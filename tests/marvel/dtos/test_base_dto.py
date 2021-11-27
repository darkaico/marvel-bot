import pytest
from dacite import from_dict

from app.marvel.dtos.base import MarvelResourceDTO


@pytest.fixture
def basic_marvel_dto():

    return from_dict(
        data_class=MarvelResourceDTO,
        data={
            "id": 7,
            "thumbnail": {
                "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/60/537bcaef0f6cf",
                "extension": "jpg",
            },
            "urls": [],
        },
    )


@pytest.fixture
def marvel_dto_with_urls():

    return from_dict(
        data_class=MarvelResourceDTO,
        data={
            "id": 7,
            "thumbnail": {
                "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/60/477bcaef0f6cf",
                "extension": "jpg",
            },
            "urls": [
                {"type": "detail", "url": "detail_url"},
                {"type": "wiki", "url": "wiki_url"},
                {"type": "comiclink", "url": "comiclink_url"},
            ],
        },
    )


@pytest.fixture
def marvel_dtos():

    dto_one = from_dict(
        data_class=MarvelResourceDTO,
        data={
            "id": 1,
            "thumbnail": {
                "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/60/487bcaef0f6cf",
                "extension": "jpg",
            },
            "urls": [
                {"type": "detail", "url": "detail_url"},
            ],
        },
    )
    dto_two = from_dict(
        data_class=MarvelResourceDTO,
        data={
            "id": 2,
            "thumbnail": {
                "path": "http://i.annihil.us/u/prod/marvel/i/mg/2/60/497bcaef0f6cf",
                "extension": "jpg",
            },
            "urls": [
                {"type": "wiki", "url": "wiki_url"},
            ],
        },
    )

    return [dto_one, dto_two]


def test_basic_dto_id(basic_marvel_dto):
    assert isinstance(basic_marvel_dto.id, int)


def test_basic_dto_urls(basic_marvel_dto):
    assert len(basic_marvel_dto.urls) == 0


def test_dto_urls(marvel_dto_with_urls):
    assert len(marvel_dto_with_urls.urls) == 3


def test_dto_urls_single(marvel_dtos):
    assert marvel_dtos[0].detail_link is not None
    assert marvel_dtos[1].wiki_link is not None
