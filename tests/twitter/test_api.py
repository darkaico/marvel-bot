from dataclasses import dataclass

import pytest
from faker import Faker
from tweepy import API

from app.twitter.api import TwitterAPI

fake = Faker()


@dataclass
class MockTweet:

    id: int
    text: str


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


def test_get_timeline():
    api = TwitterAPI.instance()

    assert isinstance(api.get_timeline(), list)


def test_api_update_status():
    api = TwitterAPI.instance()
    status = "Hola amigos"

    assert api.update_status(status).text == "Hola amigos"


def test_api_update_with_media():
    api = TwitterAPI.instance()
    status = "Twitt with media"

    assert api.update_with_media(status=status, filename="", file=None).text == status


def test_api_destroy_status():
    api = TwitterAPI.instance()

    assert api.destroy_status(2).id == 2
