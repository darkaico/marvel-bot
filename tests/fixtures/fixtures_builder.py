import json
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_wolverine_list_response():

    with open(f"{CURRENT_DIR}/wolverine_list_response.json") as f:
        wolverine_list_response = json.load(f)

    return wolverine_list_response


def get_character_no_image_response():

    with open(f"{CURRENT_DIR}/character_no_image_response.json") as f:
        character_response = json.load(f)

    return character_response


def get_comics_response():
    with open(f"{CURRENT_DIR}/comics_response.json") as f:
        comics_response = json.load(f)

    return comics_response


def get_single_character_list_response():
    with open(f"{CURRENT_DIR}/single_character_list_response.json") as f:
        response = json.load(f)

    return response


def get_single_event_list_response():
    with open(f"{CURRENT_DIR}/single_event_list_response.json") as f:
        response = json.load(f)

    return response


def get_single_comic_list_response():
    with open(f"{CURRENT_DIR}/single_comic_list_response.json") as f:
        response = json.load(f)

    return response


def get_events_response():
    with open(f"{CURRENT_DIR}/two_events_response.json") as f:
        events_response = json.load(f)

    return events_response


def get_single_resource_response(resource_name):
    response_by_name = {
        "characters": get_single_character_list_response,
        "comics": get_single_comic_list_response,
        "events": get_single_event_list_response,
    }

    return response_by_name[resource_name]()
