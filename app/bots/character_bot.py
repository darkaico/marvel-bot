import os
import time
from threading import Thread

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class CharacterBot(LoggerMixin, Thread):

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

    def get_character(self):
        marvel_character = self.marvel_api.get_random_character()
        if marvel_character.thumbnail.is_available():
            return marvel_character

        return self.get_character()

    def run(self):
        while True:
            marvel_character = self.get_character()

            self.logger.info(f'Tweeting about: {marvel_character}')

            tw_status = self.twitter_api.update_with_media(
                status=marvel_character.twitter_status,
                filename=marvel_character.thumbnail.name,
                file=marvel_character.thumbnail.image_data
            )

            self.logger.info("sleeping...")

            time.sleep(self.tweet_time)
