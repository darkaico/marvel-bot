import json

import pytest

from app.marvel.dtos import (
    EventDTO,
    dto_builders
)
from tests.fixtures.fixtures_builder import (
    get_events_response,
    get_single_event_list_response
)


@pytest.fixture
def events_dto():
    events_response = get_events_response()

    return dto_builders.build_events_from_api_response(events_response)


@pytest.fixture
def event_dto():
    event_response = get_single_event_list_response()

    return dto_builders.build_event_from_api_response(event_response)


def test_events_list(events_dto):
    assert len(events_dto) == 2


def test_event_str(event_dto):

    assert event_dto.title in str(event_dto)


def test_event_status(event_dto):

    assert 'What do you know about "Age of Apocalypse"' in event_dto.twitter_status


def test_short_description(event_dto):

    assert len(event_dto.short_description) == 200
