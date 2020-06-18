from dataclasses import dataclass

import pytest
from faker import Faker
from tweepy import API

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI

fake = Faker()


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


@dataclass
class MockStatus:

    id: int
    text: str


@pytest.fixture
def twitter_api_mock(monkeypatch):

    def mock_get_timeline(self):

        return [
            MockStatus(id=status_id, text=fake.paragraph())
            for status_id in range(fake.random_int(max=20))
        ]

    def mock_update_status(self, status, in_reply_to_status_id=None):

        return MockStatus(id=fake.random_int(), text=status)

    def mock_update_with_media(self, status, filename, file, in_reply_to_status_id=None):

        return MockStatus(id=fake.random_int(), text=status)

    def mock_destroy(self, status_id):

        return MockStatus(id=status_id, text=fake.paragraph())

    twitter_api = TwitterAPI(
        consumer_api_key='',
        consumer_api_secret_key='',
        access_token='',
        access_token_secret='',
    )

    monkeypatch.setattr(API, 'user_timeline', mock_get_timeline)
    monkeypatch.setattr(API, 'update_status', mock_update_status)
    monkeypatch.setattr(API, 'update_with_media', mock_update_with_media)
    monkeypatch.setattr(API, 'destroy_status', mock_destroy)

    return twitter_api


@pytest.fixture
def marvel_api_mock():

    marvel_api = MarvelAPI(
        public_key='',
        private_key='',
    )

    return marvel_api
