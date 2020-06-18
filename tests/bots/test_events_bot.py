from dataclasses import dataclass

import pytest

from app.bots import EventsBot
from app.marvel.api import MarvelAPI


@dataclass
class MockAvailableThumbnail:

    def is_available(self):
        return True


@dataclass
class MockEvent:

    thumbnail: object


@pytest.fixture
def events_bot(monkeypatch):

    def mock_get_valid_event(self):
        return MockEvent(
            thumbnail=MockAvailableThumbnail()
        )

    monkeypatch.setattr(MarvelAPI, 'get_random_event', mock_get_valid_event)

    return EventsBot()


def test_get_random_event(events_bot):
    event = events_bot.get_random_event()

    assert event.thumbnail.is_available()
