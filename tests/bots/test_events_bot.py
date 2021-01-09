from dataclasses import dataclass

import pytest

from app.bot import EventsBot
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
class MockEvent:

    thumbnail: object

    @property
    def twitter_status(self):
        return "Tweet"


@pytest.fixture
def valid_event():
    return MockEvent(thumbnail=MockAvailableThumbnail())


@pytest.fixture
def invalid_event():
    return MockEvent(thumbnail=MockNotAvailableThumbnail())


@pytest.fixture
def events_bot(mocker, valid_event):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_event")

    MarvelAPI.get_random_event.side_effect = [valid_event]

    return EventsBot()


@pytest.fixture
def events_bot_no_image_first_time(mocker, valid_event, invalid_event):
    mocker.patch("app.marvel.api.MarvelAPI.get_random_event")

    MarvelAPI.get_random_event.side_effect = [invalid_event, valid_event]

    return EventsBot()


def test_get_random_event(events_bot):
    event = events_bot._get_random_event()

    assert event.thumbnail.is_available()


def test_get_random_event_first_invalid(events_bot_no_image_first_time):

    event = events_bot_no_image_first_time._get_random_event()

    assert event.thumbnail.is_available()


def test_tweet(events_bot, mocker):
    mocker.patch("app.twitter.api.TwitterAPI.update_with_media")

    events_bot.tweet()

    TwitterAPI.update_with_media.assert_called_once()
