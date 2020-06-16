import json

import pytest
from dacite import from_dict

from app.marvel.constants import LinkTypeEnum
from app.marvel.dtos import (
    CharacterDTO,
    ComicDTO,
    dto_builders
)
from tests.fixtures.characters import (
    get_character_no_image_response,
    get_comics_response,
    get_wolverine_list_response
)


@pytest.fixture
def wolverine_dto():
    wolverine_list_response = get_wolverine_list_response()

    return dto_builders.build_character_from_api_response(wolverine_list_response)


@pytest.fixture
def character_no_image_dto():
    character_response = get_character_no_image_response()

    return dto_builders.build_character_from_api_response(character_response)


@pytest.fixture
def comics_dtos():
    comics_response = get_comics_response()

    return dto_builders.build_comics_from_api_response(comics_response)


def test_character_no_image(character_no_image_dto):
    assert not character_no_image_dto.thumbnail.is_available()


def test_comics_list(comics_dtos):
    assert len(comics_dtos) == 4


def test_short_description(wolverine_dto):

    assert len(wolverine_dto.short_description) == 200


def test_wolverine_data(wolverine_dto):

    assert wolverine_dto.name == 'Wolverine'
    assert len(wolverine_dto.urls) == 3
    assert wolverine_dto.wiki_link.link_type == LinkTypeEnum.WIKI


def test_wolverine_status(wolverine_dto):

    assert 'Did you know about Wolverine ?' in wolverine_dto.twitter_status
