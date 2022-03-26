from dataclasses import dataclass

import pytest

from marvel_bot.core.jobs import CharactersJob
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
class MockCharacter:

    thumbnail: object

    def build_twitter_status(self, title):
        return "Tweet"

    def build_telegram_status(self, title):
        return "Markdown"


@pytest.fixture
def valid_character():
    return MockCharacter(thumbnail=MockAvailableThumbnail())


@pytest.fixture
def mock_characters_job(mocker, valid_character):
    mocker.patch("marvel_bot.marvel.api.MarvelAPI.get_random_character")

    MarvelAPI.get_random_character.side_effect = [valid_character]

    return CharactersJob()


def test_character_jobs_execute_calls(mock_characters_job, mocker):
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_with_media")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    mock_characters_job.execute()

    TwitterAPI.update_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
