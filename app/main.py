import time

from dotenv import load_dotenv

from app.bots import (
    CharactersBot,
    ComicsBot,
    EventsBot
)

load_dotenv()


def sleep_hours(hours: int):
    time.sleep(60*60*hours)


def start_bots():
    CharactersBot().start()

    sleep_hours(2)
    ComicsBot().start()

    sleep_hours(2)
    EventsBot().start()


def init():
    if __name__ == "__main__":
        start_bots()


init()
