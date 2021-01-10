from app import main
from app.core.bot import MarvelBot


def test_init(mocker):
    mocker.patch("app.main.start_bot")
    mocker.patch.object(main, "__name__", "__main__")

    main.init()

    main.start_bot.assert_called_once()


def test_start_bot(mocker):
    mocker.patch("app.core.bot.MarvelBot._schedule_jobs")
    mocker.patch("app.core.bot.MarvelBot._start_jobs")

    main.start_bot()

    MarvelBot._schedule_jobs.assert_called_once()
    MarvelBot._start_jobs.assert_called_once()
