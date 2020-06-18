import time

from app import main
from app.bots import (
    CharactersBot,
    EventsBot
)


def test_init(mocker):
    mocker.patch('app.main.start_bots')
    mocker.patch.object(main, "__name__", "__main__")

    main.init()

    main.start_bots.assert_called_once()


def test_start_bots(mocker):
    mocker.patch('app.bots.CharactersBot.start')
    mocker.patch('app.bots.EventsBot.start')
    mocker.patch('time.sleep')

    main.start_bots()

    CharactersBot.start.assert_called_once()
    time.sleep.assert_called_once()
    EventsBot.start.assert_called_once()
