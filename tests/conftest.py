import json
import os
from dataclasses import dataclass

import pytest

from app import BASE_DIR


@dataclass
class MockResponse:

    status_code: int
    content: str = ""

    def json(self):
        return {}


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """No requests allowed during tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture(autouse=True)
def test_env(monkeypatch):
    os.environ["ENV"] = "TEST"


# Events Response


@pytest.fixture(autouse=True)
def events_response():
    with open(f"{BASE_DIR}/tests/fixtures/two_events_response.json") as f:
        events_response = json.load(f)

    return events_response


@pytest.fixture(autouse=True)
def single_event_response():
    with open(f"{BASE_DIR}/tests/fixtures/single_event_response.json") as f:
        response = json.load(f)

    return response


@pytest.fixture(autouse=True)
def single_event_no_thumbnail_response():
    with open(f"{BASE_DIR}/tests/fixtures/single_event_no_thumbnail_response.json") as f:
        response = json.load(f)

    return response


# Comics Response


@pytest.fixture(autouse=True)
def comics_response():
    with open(f"{BASE_DIR}/tests/fixtures/comics_response.json") as f:
        comics_response = json.load(f)

    return comics_response


@pytest.fixture(autouse=True)
def single_comic_response():
    with open(f"{BASE_DIR}/tests/fixtures/single_comic_response.json") as f:
        response = json.load(f)

    return response


@pytest.fixture(autouse=True)
def single_comic_no_thumbnail_response():
    with open(f"{BASE_DIR}/tests/fixtures/single_comic_no_thumbnail_response.json") as f:
        response = json.load(f)

    return response


# Characters Response


@pytest.fixture(autouse=True)
def single_character_response():
    with open(f"{BASE_DIR}/tests/fixtures/single_character_response.json") as f:
        response = json.load(f)

    return response


@pytest.fixture(autouse=True)
def single_character_no_thumbnail_response():

    with open(f"{BASE_DIR}/tests/fixtures/single_character_no_thumbnail_response.json") as f:
        character_response = json.load(f)

    return character_response


@pytest.fixture(autouse=True)
def wolverine_response():

    with open(f"{BASE_DIR}/tests/fixtures/wolverine_list_response.json") as f:
        wolverine_list_response = json.load(f)

    return wolverine_list_response
