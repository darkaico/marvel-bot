from app.marvel.api import MarvelAPI
from app.twitter.api import TwitterAPI
from app.utils.logger_utils import build_logger
import calendar
import datetime

marvel_api = MarvelAPI.instance()
twitter_api = TwitterAPI.instance()
logger = build_logger("tweet_jobs")


def _get_random_character():
    marvel_character = marvel_api.get_random_character()

    if marvel_character.thumbnail.is_available():
        return marvel_character

    return _get_random_character()


def _get_random_comic():
    marvel_comic = marvel_api.get_random_comic()
    if marvel_comic.thumbnail.is_available():
        return marvel_comic

    return _get_random_comic()


def comic_job():
    marvel_comic = _get_random_comic()

    tw_status = "🎉🎉🎉 Weekly Comic 🎉🎉🎉\n"
    tw_status += "#marvel #comicoftheweek\n\n"
    tw_status += marvel_comic.twitter_status

    logger.info(f"Tweet: {tw_status}")

    # twitter_api.update_with_media(
    #     status=tw_status,
    #     filename=marvel_comic.thumbnail.name,
    #     file=marvel_comic.thumbnail.image_data,
    # )


def character_job():
    marvel_character = _get_random_character()

    tw_status = f"🎉🎉🎉 {get_weekday()} Character 🎉🎉🎉\n"
    tw_status += marvel_character.twitter_status

    logger.info(f"Tweet: {tw_status}")

    # tw_status = twitter_api.update_with_media(
    #     status=tw_status,
    #     filename=marvel_character.thumbnail.name,
    #     file=marvel_character.thumbnail.image_data,
    # )


def get_weekday():
    return calendar.day_name[datetime.datetime.now().weekday()]