import hashlib
import random
import time

import requests


class MarvelAPI:

    BASE_URL = 'http://gateway.marvel.com/v1/public'
    # TODO: Figure out how to get this number updated
    CHARACTER_LIMIT = 1493

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self.ts = str(time.time())

    @property
    def hash(self):
        return hashlib.md5(f'{self.ts}{self.private_key}{self.public_key}'.encode('utf-8')).hexdigest()

    def _build_url(self, resource):
        return f'{self.BASE_URL}/{resource}?ts={self.ts}&hash={self.hash}&apikey={self.public_key}'

    def get_random_character(self):
        character_url = self._build_url('characters')
        random_url = f'{character_url}&limit=1&offset={random.randint(0, self.CHARACTER_LIMIT)}'

        response = requests.get(random_url)

        return response.json()
