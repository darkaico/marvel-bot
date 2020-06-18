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

    def _generate_ts(self) -> float:
        return time.time()

    def _generate_hash_token(self, ts: float) -> str:
        return hashlib.md5(f'{ts}{self.private_key}{self.public_key}'.encode('utf-8')).hexdigest()

    def _build_api_url(self, resource: str, limit: int = marvel_constants.DEFAULT_API_LIMIT) -> str:
        ts = self._generate_ts()
        hash_token = self._generate_hash_token(ts)

        return f'{self.BASE_URL}/{resource}?ts={ts}&hash={hash_token}&apikey={self.public_key}&limit={limit}'

    def get(self, resource_url: str, params: dict = None) -> dict:
        return requests.get(resource_url, params=params).json()

    def _generate_random_offset(self, resource_url: str) -> int:
        """Obtain random offset based on objects total count of specified resource url

        :param resource_url: API Url of the Marvel resource list
        """
        # Make a simple call using limit of 1
        json_response = self.get(resource_url, {'limit': 1})
        # Obtain total objects for the resource
        object_size = json_response['data']['total']
        # Generate random offset
        random_offset = random.randint(0, object_size - 1)

        return random_offset

    def _get_random_resource_response(self, resource_name: str) -> dict:
        """Obtain random resource object for the specified resource url

        :param resource_name: Marvel resource name
        """
        resource_url = self._build_api_url(resource_name)
        random_offset = self._generate_random_offset(resource_url)
        json_resource_response = self.get(resource_url, params={'limit': 1, 'offset': random_offset})

        return json_resource_response

    def get_random_character(self) -> CharacterDTO:
        json_response = self._get_random_resource_response('characters')

        return dto_builders.build_character_from_api_response(json_response)

    def get_random_event(self) -> EventDTO:
        json_response = self._get_random_resource_response('events')

        return dto_builders.build_event_from_api_response(json_response)
