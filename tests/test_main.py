from app import main
from app.core.bot import MarvelBot
from app.twitter.api import TwitterAPI
from app.telegram.api import TelegramAPI


def test_init(mocker):
    mocker.patch("app.main.start_bot")
    mocker.patch.object(main, "__name__", "__main__")

    main.init()

    main.start_bot.assert_called_once()


def test_start_bot(mocker):
    mocker.patch("app.core.bot.MarvelBot._schedule_jobs")
    mocker.patch("app.core.bot.MarvelBot._start_jobs")
    mocker.patch("app.twitter.api.TwitterAPI.update_status")
    mocker.patch("app.telegram.api.TelegramAPI.send_message")

    main.start_bot()

    MarvelBot._schedule_jobs.assert_called_once()
    MarvelBot._start_jobs.assert_called_once()
    TwitterAPI.update_status.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
