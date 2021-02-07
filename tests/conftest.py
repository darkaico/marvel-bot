import os
from dataclasses import dataclass

import pytest


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
