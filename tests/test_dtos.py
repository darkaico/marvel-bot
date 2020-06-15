import json

import pytest
from dacite import from_dict

from app.marvel.dtos import CharacterDTO
from tests.fixtures.characters import get_character_no_image


@pytest.fixture
def character_no_image_dto():
    character_data = get_character_no_image()

    return from_dict(data_class=CharacterDTO, data=character_data)


def test_character_no_image(character_no_image_dto):
    assert not character_no_image_dto.thumbnail.is_available()
