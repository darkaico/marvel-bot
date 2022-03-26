import calendar
import datetime

from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI
from marvel_bot.utils.mixins import LoggerMixin


class MarvelJob(LoggerMixin):
    def __init__(self):
        self.marvel_api = MarvelAPI.instance()
        self.twitter_api = TwitterAPI.instance()
        self.telegram_api = TelegramAPI.instance()

    @property
    def weekday(self):
        return calendar.day_name[datetime.datetime.now().weekday()]

    def execute(self):
        raise NotImplementedError()
