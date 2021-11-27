from datetime import datetime

from dacite import Config, from_dict

from app.marvel.dtos import CharacterDTO, ComicDTO, EventDTO


def build_character_from_api_response(api_response: dict):
    character_data = api_response["data"]["results"][0]

    return from_dict(
        data_class=CharacterDTO,
        data=character_data,
    )


def build_event_from_api_response(api_response: dict):
    event_data = api_response["data"]["results"][0]

    return from_dict(
        data_class=EventDTO,
        data=event_data,
        config=Config(type_hooks={datetime: lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")}),
    )


def build_events_from_api_response(events_response: dict):
    result = []

    for events_data in events_response["data"]["results"]:
        result.append(
            from_dict(
                data_class=EventDTO,
                data=events_data,
                config=Config(
                    type_hooks={datetime: lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")}
                ),
            )
        )

    return result


def build_comic_from_api_response(api_response: dict):
    comic_data = api_response["data"]["results"][0]

    return from_dict(
        data_class=ComicDTO,
        data=comic_data,
    )


def build_comics_from_api_response(comics_response: dict):
    result = []

    for comics_data in comics_response["data"]["results"]:
        result.append(from_dict(data_class=ComicDTO, data=comics_data))

    return result
