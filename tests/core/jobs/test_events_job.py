from dataclasses import dataclass

import pytest

from app.core.jobs import EventsJob
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
class MockEvent:

    thumbnail: object

    def build_twitter_status(self, title):
        return "Tweet"

    def build_telegram_status(self, title):
        return "Markdown"


@pytest.fixture
def valid_event():
    return MockEvent(thumbnail=MockAvailableThumbnail())


@pytest.fixture
def invalid_event():
    return MockEvent(thumbnail=MockNotAvailableThumbnail())


@pytest.fixture
def events_job(mocker, valid_event):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_event")

    MarvelAPI.get_random_event.side_effect = [valid_event]

    return EventsJob()


@pytest.fixture
def events_job_no_image_first_time(mocker, valid_event, invalid_event):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_event")

    MarvelAPI.get_random_event.side_effect = [invalid_event, valid_event]

    return EventsJob()


def test_get_random_event(events_job):
    event = events_job._get_random_event()

    assert event.thumbnail.is_available()


def test_get_random_event_first_invalid(events_job_no_image_first_time):

    event = events_job_no_image_first_time._get_random_event()

    assert event.thumbnail.is_available()


def test_tweet(events_job, mocker):
    mocker.patch("app.twitter.api.TwitterAPI.update_with_media")
    mocker.patch("app.telegram.api.TelegramAPI.send_message")

    events_job.execute()

    TwitterAPI.update_with_media.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
