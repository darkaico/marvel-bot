from dataclasses import dataclass

import pytest

from marvel_bot.core.jobs import ComicsJob
from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI


@dataclass
class MockAvailableThumbnail:

    name: str = ""
    image_data: object = None

    def is_available(self):
        return True


@dataclass
class MockComic:

    thumbnail: object

    def build_twitter_status(self, title):
        return "Tweet"

    def build_telegram_status(self, title):
        return "Markdown"


@pytest.fixture
def valid_comic():
    return MockComic(thumbnail=MockAvailableThumbnail())


@pytest.fixture
def mock_comics_job(mocker, valid_comic):
    mocker.patch("marvel_bot.marvel.api.MarvelAPI.get_random_comic")

    MarvelAPI.get_random_comic.side_effect = [valid_comic]

    return ComicsJob()


def test_comics_job_execute_calls(mock_comics_job, mocker):
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_with_media")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    mock_comics_job.execute()

    TwitterAPI.update_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
