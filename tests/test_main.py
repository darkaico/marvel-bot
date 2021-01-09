import time

from app import main
from app.core import CharactersBot, ComicsBot, EventsBot


def test_init(mocker):
    mocker.patch("app.main.start_bots")
    mocker.patch.object(main, "__name__", "__main__")

    main.init()

    main.start_bots.assert_called_once()


def test_start_bots(mocker):
    mocker.patch("app.core.CharactersBot.start")
    mocker.patch("app.core.EventsBot.start")
    mocker.patch("app.core.ComicsBot.start")
    mocker.patch("time.sleep")

    main.start_bots()

    CharactersBot.start.assert_called_once()
    EventsBot.start.assert_called_once()
    ComicsBot.start.assert_called_once()

    time.sleep.assert_called()
