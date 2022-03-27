import pytest
import requests

from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.marvel.dtos import CharacterDTO, ComicDTO, EventDTO
from tests.conftest import MockResponse


@pytest.fixture
def marvel_api_mock():
    return MarvelAPI()


def test_marvel_api_hash(marvel_api_mock):

    assert isinstance(marvel_api_mock._generate_hash_token(1), str)


def test_marvel_ts_generation(marvel_api_mock):

    assert isinstance(marvel_api_mock._generate_ts(), float)


def test_same_hashes_same_ts_each_call(marvel_api_mock):
    ts = 47
    hash_one = marvel_api_mock._generate_hash_token(ts)
    hash_two = marvel_api_mock._generate_hash_token(ts)

    assert hash_one == hash_two


def test_different_hashes_different_ts_each_call(marvel_api_mock):
    ts_one = 47
    hash_one = marvel_api_mock._generate_hash_token(ts_one)

    ts_two = 74
    hash_two = marvel_api_mock._generate_hash_token(ts_two)

    assert hash_one != hash_two


def test_build_api_url(marvel_api_mock):

    base_url = marvel_api_mock._build_api_url("comics")

    assert "https://gateway.marvel.com/v1/public/comics" in base_url


def test_build_api_url_different_each_time(marvel_api_mock):

    base_url_one = marvel_api_mock._build_api_url("events")
    base_url_two = marvel_api_mock._build_api_url("events")

    assert base_url_one != base_url_two


def mock_get_random_offset_response(resource_url, params):
    return {"data": {"total": 10000}}


def test_get_method(marvel_api_mock, monkeypatch):
    monkeypatch.setattr(
        requests, "get", lambda url, params: MockResponse(content="", status_code=200)
    )

    assert isinstance(marvel_api_mock.get(""), dict)


def test_generate_random_offset(marvel_api_mock, monkeypatch):
    monkeypatch.setattr(marvel_api_mock, "get", mock_get_random_offset_response)

    assert isinstance(marvel_api_mock._generate_random_offset("characters"), int)


def test_generate_random_offset_randomless(marvel_api_mock, monkeypatch):
    monkeypatch.setattr(marvel_api_mock, "get", mock_get_random_offset_response)

    offset_one = marvel_api_mock._generate_random_offset("characters")
    offset_two = marvel_api_mock._generate_random_offset("characters")

    assert offset_one != offset_two


def test_get_random_resource_response(marvel_api_mock, monkeypatch):
    monkeypatch.setattr(marvel_api_mock, "_generate_random_offset", lambda x: 4)
    monkeypatch.setattr(marvel_api_mock, "get", mock_get_random_offset_response)

    assert isinstance(marvel_api_mock._get_random_resource_response("characters"), dict)


def test_get_random_event(marvel_api_mock, mocker, single_event_response):
    mocker.patch.object(marvel_api_mock, "_get_random_resource_response")
    marvel_api_mock._get_random_resource_response.side_effect = [single_event_response]

    event_dto = marvel_api_mock.get_random_event()

    assert isinstance(event_dto, EventDTO)
    assert event_dto.thumbnail.is_available()


def test_get_random_comic(marvel_api_mock, mocker, single_comic_response):
    mocker.patch.object(marvel_api_mock, "_get_random_resource_response")
    marvel_api_mock._get_random_resource_response.side_effect = [single_comic_response]

    comic_dto = marvel_api_mock.get_random_comic()

    assert isinstance(comic_dto, ComicDTO)
    assert comic_dto.thumbnail.is_available()


def test_get_random_character(marvel_api_mock, mocker, single_character_response):
    mocker.patch.object(marvel_api_mock, "_get_random_resource_response")
    marvel_api_mock._get_random_resource_response.side_effect = [single_character_response]

    character_dto = marvel_api_mock.get_random_character()

    assert isinstance(character_dto, CharacterDTO)
    assert character_dto.thumbnail.is_available()
