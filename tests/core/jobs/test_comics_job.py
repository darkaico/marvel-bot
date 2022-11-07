import pytest

from marvel_bot.core.jobs import ComicsJob
from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI
from tests.factories import ComicDTOFactory


@pytest.fixture
def valid_comic():
    return ComicDTOFactory()


@pytest.fixture
def mock_comics_job(mocker, valid_comic):
    mocker.patch.object(MarvelAPI, "get_random_comic")

    MarvelAPI.get_random_comic.side_effect = [valid_comic]

    return ComicsJob()


def test_comics_job_execute_calls(mock_comics_job, mocker):
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_status_with_media")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    mock_comics_job.execute()

    TwitterAPI.update_status_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
