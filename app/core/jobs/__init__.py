from app.utils.mixins import LoggerMixin
from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
import calendar
import datetime


class MarvelJob(LoggerMixin):
    logger_name = "marvel_jobs"

    def __init__(self):
        self.marvel_api = MarvelAPI.instance()
        self.twitter_api = TwitterAPI.instance()

    @property
    def weekday(self):
        return calendar.day_name[datetime.datetime.now().weekday()]

    def execute(self):
        raise NotImplementedError()