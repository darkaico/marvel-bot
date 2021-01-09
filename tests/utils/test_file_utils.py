from dataclasses import dataclass
from io import BytesIO

import requests

from app.utils import file_utils
from tests.conftest import MockResponse


def test_file(monkeypatch):
    def mock_get_content(url):
        return MockResponse(content=None, status_code=200)

    monkeypatch.setattr(requests, "get", mock_get_content)

    assert isinstance(file_utils.build_image_from_url("url"), BytesIO)
