from marvel_bot import main
from marvel_bot.core.bot import MarvelBot
from marvel_bot.telegram.api import TelegramAPI
from marvel_bot.twitter.api import TwitterAPI


def test_init(mocker):
    mocker.patch("marvel_bot.main.start_bot")
    mocker.patch.object(main, "__name__", "__main__")

    main.init()

    main.start_bot.assert_called_once()


def test_start_bot(mocker):
    mocker.patch("marvel_bot.core.bot.MarvelBot._schedule_jobs")
    mocker.patch("marvel_bot.core.bot.MarvelBot._start_jobs")
    mocker.patch("marvel_bot.twitter.api.TwitterAPI.update_status")
    mocker.patch("marvel_bot.telegram.api.TelegramAPI.send_message")

    main.start_bot()

    MarvelBot._schedule_jobs.assert_called_once()
    MarvelBot._start_jobs.assert_called_once()
    TwitterAPI.update_status.assert_called_once()
    TelegramAPI.send_message.assert_called_once()
