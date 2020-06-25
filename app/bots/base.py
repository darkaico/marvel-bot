import calendar
import datetime
import os
import random
import time
from threading import Thread

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class MarvelBot(LoggerMixin, Thread):

    tweet_interval = 60 * 60 * 6
    logger_name = 'marvel_bots'

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
    def weekday(self):
        return calendar.day_name[datetime.datetime.now().weekday()]

    def generate_tweet_time(self):
        random_time = 60 * random.randint(-60, 60)

        return self.tweet_interval + random_time

    def wait_for_tweet(self):
        self.logger.info(f'sleeping {self.tweet_interval} hours...')

        time.sleep(self.generate_tweet_time())

    def run(self):
        while True:
            self.tweet()
            self.wait_for_tweet()

    def tweet(self):
        raise NotImplementedError()
