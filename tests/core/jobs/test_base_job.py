from unittest.mock import patch

import pytest

from marvel_bot.core.jobs.base import MarvelJob


@pytest.fixture
def mock_marvel_job():
    return MarvelJob()


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


# def test_get_random_resource_valid_first_time(mocker, mock_marvel_job):
#     mocker.patch.object(mock_marvel_job, "get_resource")
#     mock_marvel_job.get_resource.side_effect = [valid_resrouce]
#     random_resource_dto = mock_marvel_job.get_random_resource()

#     assert isinstance(random_resource_dto, MarvelResourceDTO)
#     assert random_resource_dto.thumbnail.is_available()


# def test_get_random_resource_valid_second_time(mock_marvel_job):

#     random_resource_dto = mock_marvel_job.get_random_resource()

#     assert isinstance(random_resource_dto, MarvelResourceDTO)
#     assert random_resource_dto.thumbnail.is_available()


# @pytest.mark.skip("Include stop iteration")
# def test_get_random_comic_always_invalid(
#     marvel_api_mock, mocker, single_comic_no_thumbnail_response
# ):
#     mocker.patch.object(marvel_api_mock, "_get_random_resource_response")
#     marvel_api_mock._get_random_resource_response.side_effect = [
#         single_comic_no_thumbnail_response
#     ]

#     comic_dto = marvel_api_mock.get_random_comic()

#     assert isinstance(comic_dto, ComicDTO)
#     assert comic_dto.thumbnail.is_available()
