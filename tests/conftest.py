import os
from dataclasses import dataclass

import pytest
from faker import Faker
from tweepy import API

fake = Faker()


@dataclass
class MockResponse:

    content: str
    status_code: int

    def json(self):
        return {}


@dataclass
class MockTweet:

    id: int
    text: str


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """No requests allowed during tests."""
    monkeypatch.delattr("requests.sessions.Session.request")


@pytest.fixture(autouse=True)
def mock_tweepy_api(monkeypatch):
    def mock_get_timeline(self):

        return [
            MockTweet(id=status_id, text=fake.paragraph())
            for status_id in range(fake.random_int(max=20))
        ]

    def mock_update_status(self, status, in_reply_to_status_id=None):

        return MockTweet(id=fake.random_int(), text=status)

    def mock_update_with_media(self, status, filename, file, in_reply_to_status_id=None):

        return MockTweet(id=fake.random_int(), text=status)

    def mock_destroy(self, status_id):

        return MockTweet(id=status_id, text=fake.paragraph())

    monkeypatch.setattr(API, "user_timeline", mock_get_timeline)
    monkeypatch.setattr(API, "update_status", mock_update_status)
    monkeypatch.setattr(API, "update_with_media", mock_update_with_media)
    monkeypatch.setattr(API, "destroy_status", mock_destroy)


@pytest.fixture(autouse=True)
def test_env(monkeypatch):
    os.environ["ENV"] = "TEST"
