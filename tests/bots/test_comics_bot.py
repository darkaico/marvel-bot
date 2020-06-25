from dataclasses import dataclass

import pytest

from app.bots import ComicsBot
from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI


@dataclass
class MockAvailableThumbnail:

    name: str = ''
    image_data: object = None

    def is_available(self):
        return True


@dataclass
class MockNotAvailableThumbnail:

    name: str = ''
    image_data: object = None

    def is_available(self):
        return False


@dataclass
class MockComic:

    thumbnail: object

    @property
    def twitter_status(self):
        return 'Tweet'


@pytest.fixture
def valid_comic():
    return MockComic(
        thumbnail=MockAvailableThumbnail()
    )


@pytest.fixture
def invalid_comic():
    return MockComic(
        thumbnail=MockNotAvailableThumbnail()
    )


@pytest.fixture
def comics_bot(mocker, valid_comic):
    mocker.patch('app.marvel.api.MarvelAPI.get_random_comic')

    MarvelAPI.get_random_comic.side_effect = [valid_comic]

    return ComicsBot()


@pytest.fixture
def comics_bot_no_image_first_time(mocker, valid_comic, invalid_comic):
    mocker.patch('app.marvel.api.MarvelAPI.get_random_comic')

    MarvelAPI.get_random_comic.side_effect = [invalid_comic, valid_comic]

    return ComicsBot()


def test_get_random_comic(comics_bot):
    comic = comics_bot._get_random_comic()

    assert comic.thumbnail.is_available()


def test_get_random_comic_first_invalid(comics_bot_no_image_first_time):

    comic = comics_bot_no_image_first_time._get_random_comic()

    assert comic.thumbnail.is_available()


def test_tweet(comics_bot, mocker):
    mocker.patch('app.twitter.api.TwitterAPI.update_with_media')

    comics_bot.tweet()

    TwitterAPI.update_with_media.assert_called_once()
