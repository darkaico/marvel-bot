from io import BytesIO

import pytest
import requests

from app.marvel.dtos import ImageDTO
from tests.conftest import MockResponse


@pytest.fixture
def image_dto():
    return ImageDTO("", "")


def test_image_data(image_dto, monkeypatch):
    def mock_get_content(url):
        return MockResponse(content=None, status_code=200)

    monkeypatch.setattr(requests, "get", mock_get_content)

    assert isinstance(image_dto.image_data, BytesIO)
