import hashlib
import random
import time

import requests

from app import marvel as marvel_constants
from app.marvel import builders


class MarvelAPI:

    BASE_URL = 'http://gateway.marvel.com/v1/public'

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.ts = str(time.time())

    @property
    def hash(self):
        return hashlib.md5(f'{self.ts}{self.private_key}{self.public_key}'.encode('utf-8')).hexdigest()

    def _build_url(self, resource: str, limit: int = marvel_constants.DEFAULT_API_LIMIT):
        return f'{self.BASE_URL}/{resource}?ts={self.ts}&hash={self.hash}&apikey={self.public_key}&limit={limit}'

    def get_random_character(self):
        character_url = self._build_url('characters')
        random_url = f'{character_url}&limit=1&offset={random.randint(0, marvel_constants.CHARACTER_LIMIT)}'

        response = requests.get(random_url)

        return builders.build_character_from_api_response(response.json())

    def get_character_comics(self, character_id: int, limit: int = marvel_constants.DEFAULT_API_LIMIT):
        comics_url = self._build_url(f'characters/{character_id}/comics', limit=limit)

        response = requests.get(comics_url)

        return builders.build_comics_from_api_response(response.json())
