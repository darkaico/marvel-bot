import pytest

from marvel_bot.core.jobs import EventsJob
from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI
from tests.factories import EventDTOFactory


@pytest.fixture
def valid_event():
    return EventDTOFactory()


@pytest.fixture
def mock_events_job(mocker, valid_event):
    mocker.patch.object(MarvelAPI, "get_random_event")

    MarvelAPI.get_random_event.side_effect = [valid_event]

    return EventsJob()


def test_events_job_execute_calls(mock_events_job, mocker):
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_status_with_media")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    mock_events_job.execute()

    TwitterAPI.update_status_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
