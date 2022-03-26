import pytest

from marvel_bot.marvel.constants import LinkTypeEnum
from marvel_bot.marvel.dtos import dto_builders


@pytest.fixture
def wolverine_dto(wolverine_response):

    return dto_builders.build_character_from_api_response(wolverine_response)


@pytest.fixture
def character_no_image_dto(single_character_no_thumbnail_response):

    return dto_builders.build_character_from_api_response(single_character_no_thumbnail_response)


def test_character_no_image(character_no_image_dto):
    assert not character_no_image_dto.thumbnail.is_available()


def test_short_description(wolverine_dto):

    assert len(wolverine_dto.short_description) == 200


def test_wolverine_str(wolverine_dto):

    assert "Wolverine" in str(wolverine_dto)


def test_wolverine_data(wolverine_dto):

    assert wolverine_dto.name == "Wolverine"
    assert len(wolverine_dto.urls) == 3
    assert wolverine_dto.wiki_link.link_type == LinkTypeEnum.WIKI


def test_wolverine_status(wolverine_dto):

    assert "Did you know about Wolverine ?" in wolverine_dto.build_twitter_status("title")
