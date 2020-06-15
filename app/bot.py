import os
import time

from dotenv import load_dotenv

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI

load_dotenv()


class MarvelBot:

    def __init__(self):
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

    def run(self):
        while True:
            marvel_character = self.marvel_api.get_random_character()

            self.twitter_api.update_with_media(
                status=marvel_character.twitter_status,
                filename=marvel_character.thumbnail.name,
                file=marvel_character.thumbnail.image_data
            )

            print("Sleeping 1 hour...")

            time.sleep(15)


if __name__ == "__main__":
    MarvelBot().run()
