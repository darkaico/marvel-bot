from dataclasses import dataclass

import pytest

from app.core.jobs import ComicsJob
from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.telegram.api import TelegramAPI


@dataclass
class MockAvailableThumbnail:

    name: str = ""
    image_data: object = None

    def is_available(self):
        return True


@dataclass
class MockNotAvailableThumbnail:

    name: str = ""
    image_data: object = None

    def is_available(self):
        return False


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
def invalid_comic():
    return MockComic(thumbnail=MockNotAvailableThumbnail())


@pytest.fixture
def comics_job(mocker, valid_comic):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_comic")

    MarvelAPI.get_random_comic.side_effect = [valid_comic]

    return ComicsJob()


@pytest.fixture
def comics_job_no_image_first_time(mocker, valid_comic, invalid_comic):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_comic")

    MarvelAPI.get_random_comic.side_effect = [invalid_comic, valid_comic]

    return ComicsJob()


def test_get_random_comic(comics_job):
    comic = comics_job._get_random_comic()

    assert comic.thumbnail.is_available()


def test_get_random_comic_first_invalid(comics_job_no_image_first_time):

    comic = comics_job_no_image_first_time._get_random_comic()

    assert comic.thumbnail.is_available()


def test_tweet(comics_job, mocker):
    mocker.patch("app.twitter.api.TwitterAPI.update_with_media")
    mocker.patch("app.telegram.api.TelegramAPI.send_message")

    comics_job.execute()

    TwitterAPI.update_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
