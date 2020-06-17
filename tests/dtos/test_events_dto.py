import json

import pytest

from app.marvel.dtos import (
    EventDTO,
    dto_builders
)
from tests.fixtures.fixtures_builder import get_events_response


@pytest.fixture
def events_dto():
    events_response = get_events_response()

    return dto_builders.build_events_from_api_response(events_response)


def test_events_list(events_dto):
    assert len(events_dto) == 2


def test_event_status(events_dto):

    assert 'What do you know about "Onslaught"' in events_dto[0].twitter_status
