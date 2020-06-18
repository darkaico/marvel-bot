from dataclasses import dataclass

import pytest

from app.bots import CharactersBot
from app.marvel.api import MarvelAPI


@dataclass
class MockAvailableThumbnail:

    def is_available(self):
        return True


@dataclass
class MockCharacter:

    thumbnail: object


@pytest.fixture
def character_bot(monkeypatch):

    def mock_get_valid_character(self):
        return MockCharacter(
            thumbnail=MockAvailableThumbnail()
        )

    monkeypatch.setattr(MarvelAPI, 'get_random_character', mock_get_valid_character)

    return CharactersBot()


def test_get_random_character(character_bot):
    character = character_bot.get_random_character()

    assert character.thumbnail.is_available()
