from dataclasses import dataclass

import pytest

from app.bots import ComicsBot
from app.marvel.api import MarvelAPI


@dataclass
class MockAvailableThumbnail:

    def is_available(self):
        return True


@dataclass
class MockComic:

    thumbnail: object


@pytest.fixture
def comics_bot(monkeypatch):

    def mock_get_valid_comic(self):
        return MockComic(
            thumbnail=MockAvailableThumbnail()
        )

    monkeypatch.setattr(MarvelAPI, 'get_random_comic', mock_get_valid_comic)

    return ComicsBot()


def test_get_random_comic(comics_bot):
    comic = comics_bot.get_random_comic()

    assert comic.thumbnail.is_available()
