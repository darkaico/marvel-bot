from dacite import (
    Config,
    from_dict
)

from app.marvel.dtos import (
    CharacterDTO,
    ComicDTO
)


def build_character_from_api_response(api_response: dict):
    character_data = api_response['data']['results'][0]

    return from_dict(
        data_class=CharacterDTO,
        data=character_data,
    )


def build_comics_from_api_response(comics_response: dict):
    result = []

    for comics_data in comics_response['data']['results']:
        result.append(from_dict(data_class=ComicDTO, data=comics_data))

    return result
