import calendar
import datetime
import random
import time
from threading import Thread

from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class MarvelBot(LoggerMixin, Thread):

    tweet_interval = 60 * 60 * 24
    logger_name = "marvel_bots"

    def __init__(self):
        Thread.__init__(self)

        self.marvel_api = MarvelAPI.instance()
        self.twitter_api = TwitterAPI.instance()

    @property
    def weekday(self):
        return calendar.day_name[datetime.datetime.now().weekday()]

    def generate_tweet_time(self):
        random_time = 60 * random.randint(-60, 60)

        return self.tweet_interval + random_time

    def wait_for_tweet(self):
        self.logger.info(f"sleeping {self.tweet_interval} hours...")

        time.sleep(self.generate_tweet_time())

    def run(self):
        while True:
            self.tweet()
            self.wait_for_tweet()

    def tweet(self):
        raise NotImplementedError()
