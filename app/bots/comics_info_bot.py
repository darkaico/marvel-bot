import os
import time
from threading import Thread

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class ComicsBot(LoggerMixin, Thread):

    def __init__(self):
        Thread.__init__(self)

        self.marvel_api = MarvelAPI(
            public_key=os.getenv("MARVEL_API_KEY"),
            private_key=os.getenv("MARVEL_PRIVATE_KEY")
        )

        self.twitter_api = TwitterAPI(
            os.getenv("TW_API_KEY"),
            os.getenv("TW_SECRET_KEY"),
            os.getenv("TW_ACCESS_TOKEN"),
            os.getenv("TW_ACCESS_TOKEN_SECRET"),
        )

    @property
    def tweet_time(self):
        return 60 * 60 * 2

    @property
    def comics_limit(self):
        return 4

    def get_character(self):
        marvel_character = self.marvel_api.get_random_character()
        if marvel_character.thumbnail.is_available():
            return marvel_character

        return self.get_character()

    def get_comics(self, character_id: int):
        return self.marvel_api.get_character_comics(character_id, limit=self.comics_limit)

    def run(self):
        while True:
            marvel_character = self.get_character()
            comics = self.get_comics(marvel_character.id)

            self.logger.info(f'Tweeting about: {marvel_character}')

            self.logger.info("sleeping...")

            time.sleep(self.tweet_time)
