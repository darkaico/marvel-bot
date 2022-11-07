import calendar
import datetime

from marvel_bot.marvel.api import MarvelAPI
from marvel_bot.marvel.dtos.base import MarvelResourceDTO
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI
from marvel_bot.utils.mixins import LoggerMixin


class MarvelJob(LoggerMixin):
    def __init__(self):
        self.marvel_api = MarvelAPI()
        self.twitter_api = TwitterAPI.instance()
        self.telegram_api = TelegramAPI.instance()

    @property
    def weekday(self):
        return calendar.day_name[datetime.datetime.now().weekday()]

    def get_title(self) -> MarvelResourceDTO:
        """Each Job should implement this function."""

        raise NotImplementedError

    def get_resource(self) -> MarvelResourceDTO:
        """Each Job should implement this function."""
        raise NotImplementedError

    def get_random_resource(self) -> MarvelResourceDTO:
        marvel_resource_dto = self.get_resource()

        if not marvel_resource_dto.thumbnail.is_available():
            return self.get_random_resource()

        return marvel_resource_dto

    def execute(self):
        random_resource_dto = self.get_random_resource()

        title = self.get_title()
        tw_status = random_resource_dto.build_twitter_status(title)
        telegram_status = random_resource_dto.build_telegram_status(title)

        self.logger.info(f"Tweet: {tw_status}")
        self.logger.info(f"Telegram: {telegram_status}")

        self.twitter_api.update_status_with_media(
            status=tw_status,
            filename=random_resource_dto.thumbnail.name,
            file=random_resource_dto.thumbnail.image_data,
        )

        self.telegram_api.send_message(telegram_status)
