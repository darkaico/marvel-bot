import json
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_wolverine_response():

    with open(f'{CURRENT_DIR}/wolverine_response.json') as f:
        wolverine_response = json.load(f)

    return wolverine_response


def get_character_no_image_response():

    with open(f'{CURRENT_DIR}/character_no_image_response.json') as f:
        character_response = json.load(f)

    return character_response


def get_comics_response():
    with open(f'{CURRENT_DIR}/comics_response.json') as f:
        comics_response = json.load(f)

    return comics_response
