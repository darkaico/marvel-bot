from unittest.mock import patch

import pytest

from marvel_bot.core.jobs.base import MarvelJob
from marvel_bot.core.jobs.characters_job import CharactersJob
from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.marvel.dtos import CharacterDTO
from tests.factories import CharacterDTOFactory, ImageDTONoThumbnailFactory


@pytest.fixture
def mock_marvel_job():
    return MarvelJob()


@pytest.fixture
def mock_character_marvel_job():
    return CharactersJob()


def test_execute_should_be_implemented(mock_marvel_job):
    with pytest.raises(NotImplementedError):
        mock_marvel_job.execute()


def test_weekday(mock_marvel_job):

    assert isinstance(mock_marvel_job.weekday, str)


@patch("marvel_bot.core.jobs.base.MarvelAPI")
def test_methods_must_be_implemented(mock_marvel_api):
    """Verify that every implementation of MarvelJob implements required methods."""
    for MarvelJobClass in MarvelJob.__subclasses__():
        marvel_job = MarvelJobClass()
        assert marvel_job.get_title()
        assert marvel_job.get_resource()


def test_implementation_with_no_get_title():
    class MockJobNoTitleImplementation(MarvelJob):
        pass

    marvel_job = MockJobNoTitleImplementation()
    with pytest.raises(NotImplementedError):
        marvel_job.get_title()


def test_implementation_with_no_get_resource():
    class MockJobNoGetResourceImplementation(MarvelJob):
        pass

    marvel_job = MockJobNoGetResourceImplementation()
    with pytest.raises(NotImplementedError):
        marvel_job.get_resource()


@pytest.fixture
def mock_chracter():
    return CharacterDTOFactory()


@pytest.fixture
def mock_chracter_with_no_thumbnail():
    return CharacterDTOFactory(thumbnail=ImageDTONoThumbnailFactory())


def test_get_random_resource_valid_first_time(mocker, mock_character_marvel_job, mock_chracter):
    mocker.patch.object(MarvelAPI, "get_random_character")
    MarvelAPI.get_random_character.side_effect = [mock_chracter]

    random_resource_dto = mock_character_marvel_job.get_random_resource()

    assert isinstance(random_resource_dto, CharacterDTO)
    assert random_resource_dto.thumbnail.is_available()


def test_get_random_resource_valid_second_time(
    mocker, mock_character_marvel_job, mock_chracter, mock_chracter_with_no_thumbnail
):
    mocker.patch.object(MarvelAPI, "get_random_character")
    MarvelAPI.get_random_character.side_effect = [mock_chracter_with_no_thumbnail, mock_chracter]

    random_resource_dto = mock_character_marvel_job.get_random_resource()

    assert isinstance(random_resource_dto, CharacterDTO)
    assert random_resource_dto.thumbnail.is_available()


@pytest.mark.skip("Include stop iteration")
def test_get_random_resource_always_invalid(
    mocker, mock_character_marvel_job, mock_chracter_with_no_thumbnail
):
    mocker.patch.object(MarvelAPI, "get_random_character")
    MarvelAPI.get_random_character.side_effect = [
        mock_chracter_with_no_thumbnail,
        mock_chracter_with_no_thumbnail,
    ]

    random_resource_dto = mock_character_marvel_job.get_random_resource()

    assert isinstance(random_resource_dto, CharacterDTO)
    assert random_resource_dto.thumbnail.is_available()
