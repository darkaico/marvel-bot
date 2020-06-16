import json

import pytest
from dacite import from_dict

from app.marvel import builders
from app.marvel.dtos import (
    CharacterDTO,
    ComicDTO
)
from tests.fixtures.characters import (
    get_character_no_image_response,
    get_comics_response,
    get_wolverine_response
)


@pytest.fixture
def wolverine_dto():
    character_response = get_wolverine_response()

    return builders.build_character_from_api_response(character_response)


@pytest.fixture
def character_no_image_dto():
    character_response = get_character_no_image_response()

    return builders.build_character_from_api_response(character_response)


@pytest.fixture
def comics_dtos():
    comics_response = get_comics_response()

    return builders.build_comics_from_api_response(comics_response)


def test_character_no_image(character_no_image_dto):
    assert not character_no_image_dto.thumbnail.is_available()


def test_comics_list(comics_dtos):
    assert len(comics_dtos) == 4


def test_short_description(wolverine_dto):

    assert len(wolverine_dto.short_description) == 200
