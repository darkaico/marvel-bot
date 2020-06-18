import hashlib
import random
import time

import requests

from app import marvel as marvel_constants
from app.marvel.dtos import (
    CharacterDTO,
    EventDTO,
    dto_builders
)


class MarvelAPI:

    BASE_URL = 'http://gateway.marvel.com/v1/public'

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def generate_ts(self) -> float:
        return time.time()

    def generate_hash_token(self, ts: float) -> str:
        return hashlib.md5(f'{ts}{self.private_key}{self.public_key}'.encode('utf-8')).hexdigest()

    def _build_base_url(self, resource: str, limit: int = marvel_constants.DEFAULT_API_LIMIT) -> str:
        ts = self.generate_ts()
        hash_token = self.generate_hash_token(ts)

        return f'{self.BASE_URL}/{resource}?ts={ts}&hash={hash_token}&apikey={self.public_key}&limit={limit}'

    def _get_random_resource(self, resource_url: str) -> dict:
        base_url = self._build_base_url(resource_url)

        # Get object size
        base_response = requests.get(base_url, {'limit': 1})
        object_size = base_response.json()['data']['total']
        # Generate random offset
        random_offset = random.randint(0, object_size - 1)

        resource_response = requests.get(base_url, params={'limit': 1, 'offset': random_offset})

        return resource_response.json()

    def get_random_character(self) -> CharacterDTO:
        json_response = self._get_random_resource('characters')

        return dto_builders.build_character_from_api_response(json_response)

    def get_random_event(self) -> EventDTO:
        json_response = self._get_random_resource('events')

        return dto_builders.build_event_from_api_response(json_response)

    def get_character_comics(self, character_id: int, limit: int = marvel_constants.DEFAULT_API_LIMIT):
        comics_url = self._build_base_url(f'characters/{character_id}/comics', limit=limit)

        response = requests.get(comics_url)

        return dto_builders.build_comics_from_api_response(response.json())
