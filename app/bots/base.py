import calendar
import datetime
import os
import time
from threading import Thread

from cached_property import cached_property

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class MarvelBot(LoggerMixin, Thread):

    tweet_interval = 6

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

    @cached_property
    def tweet_time(self):
        return 60 * 60 * self.tweet_interval

    def wait_for_tweet(self):
        self.logger.info(f'sleeping {self.tweet_interval} hours...')

        time.sleep(self.tweet_time)
