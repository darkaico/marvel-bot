import json
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_character_no_image():

    with open(f'{CURRENT_DIR}/character_no_image.json') as f:
        character_data = json.load(f)

    return character_data
