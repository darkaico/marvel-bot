import pytest

from marvel_bot.core.jobs import CharactersJob
from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI
from tests.factories import CharacterDTOFactory


@pytest.fixture
def valid_character():
    return CharacterDTOFactory()


@pytest.fixture
def mock_characters_job(mocker, valid_character):
    mocker.patch.object(MarvelAPI, "get_random_character")

    MarvelAPI.get_random_character.side_effect = [valid_character]

    return CharactersJob()


def test_character_jobs_execute_calls(mock_characters_job, mocker):
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_status_with_media")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    mock_characters_job.execute()

    TwitterAPI.update_status_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
