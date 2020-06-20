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
class MockComic:

    thumbnail: object

    @property
    def twitter_status(self):
        return 'Tweet'


@pytest.fixture
def comics_bot(monkeypatch):

    def mock_get_valid_comic(self):
        return MockComic(
            thumbnail=MockAvailableThumbnail()
        )

    monkeypatch.setattr(MarvelAPI, 'get_random_comic', mock_get_valid_comic)

    return ComicsBot()


def test_get_random_comic(comics_bot):
    comic = comics_bot._get_random_comic()

    assert comic.thumbnail.is_available()


def test_tweet(comics_bot, mocker):
    mocker.patch('app.twitter.api.TwitterAPI.update_with_media')

    comics_bot.tweet()

    TwitterAPI.update_with_media.assert_called_once()
