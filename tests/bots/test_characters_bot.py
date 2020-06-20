from dataclasses import dataclass

import pytest

from app.bots import CharactersBot
from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI


@dataclass
class MockAvailableThumbnail:

    name: str = ''
    image_data: object = None

    def is_available(self):
        return True


@dataclass
class MockCharacter:

    thumbnail: object

    @property
    def twitter_status(self):
        return 'Tweet'


@pytest.fixture
def character_bot(monkeypatch):

    def mock_get_valid_character(self):
        return MockCharacter(
            thumbnail=MockAvailableThumbnail()
        )

    monkeypatch.setattr(MarvelAPI, 'get_random_character', mock_get_valid_character)

    return CharactersBot()


def test_get_random_character(character_bot):
    character = character_bot._get_random_character()

    assert character.thumbnail.is_available()


def test_tweet(character_bot, mocker):
    mocker.patch('app.twitter.api.TwitterAPI.update_with_media')

    character_bot.tweet()

    TwitterAPI.update_with_media.assert_called_once()
