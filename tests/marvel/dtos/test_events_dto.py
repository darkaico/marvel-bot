import pytest

from app.marvel.dtos import dto_builders


@pytest.fixture
def events_dto(events_response):

    return dto_builders.build_events_from_api_response(events_response)


@pytest.fixture
def event_dto(events_response):

    return dto_builders.build_event_from_api_response(events_response)


def test_events_list(events_dto):
    assert len(events_dto) == 2


def test_event_str(event_dto):

    assert event_dto.title in str(event_dto)


def test_event_status(event_dto):

    assert 'What do you know about "Onslaught"' in event_dto.build_twitter_status("title")


def test_short_description(event_dto):

    assert len(event_dto.short_description) == 200
