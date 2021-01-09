from dataclasses import dataclass

import pytest

from app.bot import CharactersBot
from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI


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
class MockCharacter:

    thumbnail: object

    @property
    def twitter_status(self):
        return "Tweet"


@pytest.fixture
def valid_character():
    return MockCharacter(thumbnail=MockAvailableThumbnail())


@pytest.fixture
def invalid_character():
    return MockCharacter(thumbnail=MockNotAvailableThumbnail())


@pytest.fixture
def characters_bot(mocker, valid_character):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_character")

    MarvelAPI.get_random_character.side_effect = [valid_character]

    return CharactersBot()


@pytest.fixture
def characters_bot_no_image_first_time(mocker, valid_character, invalid_character):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_character")

    MarvelAPI.get_random_character.side_effect = [invalid_character, valid_character]

    return CharactersBot()


def test_get_random_character_valid(characters_bot):

    character = characters_bot._get_random_character()

    assert character.thumbnail.is_available()


def test_get_random_character_first_invalid(characters_bot_no_image_first_time):

    character = characters_bot_no_image_first_time._get_random_character()

    assert character.thumbnail.is_available()


def test_tweet(characters_bot, mocker):
    mocker.patch("app.twitter.api.TwitterAPI.update_with_media")

    characters_bot.tweet()

    TwitterAPI.update_with_media.assert_called_once()
