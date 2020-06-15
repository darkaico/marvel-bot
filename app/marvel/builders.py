from app.marvel.dtos import CharacterDTO
from dacite import from_dict


def build_character_from_api(api_response):
    character_data = api_response['data']['results'][0]

    return from_dict(data_class=CharacterDTO, data=character_data)
