import pytest

from app.marvel.dtos import dto_builders


@pytest.fixture
def comics_dtos(comics_response):

    return dto_builders.build_comics_from_api_response(comics_response)


@pytest.fixture
def comic_dto(comics_response):

    return dto_builders.build_comic_from_api_response(comics_response)


def test_comics_list(comics_dtos):
    assert len(comics_dtos) == 4


def test_comic_str(comic_dto):

    assert comic_dto.title in str(comic_dto)


def test_comic_twitter_status(comic_dto):

    assert (
        'Have you read "X-Men: Days of Future Past (Trade Paperback)"?'
        in comic_dto.build_twitter_status("title")
    )


def test_short_description(comic_dto):

    assert len(comic_dto.short_description) == 200
