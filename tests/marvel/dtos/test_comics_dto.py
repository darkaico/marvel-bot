import json

import pytest

from app.marvel.dtos import (
    ComicDTO,
    dto_builders
)
from tests.fixtures.fixtures_builder import get_comics_response


@pytest.fixture
def comics_dtos():
    comics_response = get_comics_response()

    return dto_builders.build_comics_from_api_response(comics_response)


def test_comics_list(comics_dtos):
    assert len(comics_dtos) == 4
