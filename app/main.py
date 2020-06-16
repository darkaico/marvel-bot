import os
import time
from threading import Thread

from dotenv import load_dotenv

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin

load_dotenv()


class MarvelBot(LoggerMixin, Thread):

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

            tw_status = self.twitter_api.update_with_media(
                status=marvel_character.twitter_status,
                filename=marvel_character.thumbnail.name,
                file=marvel_character.thumbnail.image_data
            )

            last_status_id = tw_status.id
            for comic in comics:
                thread_status = self.twitter_api.update_with_media(
                    status=comic.twitter_status,
                    filename=comic.thumbnail.name,
                    file=comic.thumbnail.image_data,
                    in_reply_to_status_id=last_status_id
                )
                last_status_id = thread_status.id

            self.logger.info("sleeping...")

            time.sleep(self.tweet_time)


if __name__ == "__main__":
    MarvelBot().start()
