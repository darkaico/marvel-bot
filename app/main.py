import time

from dotenv import load_dotenv

load_dotenv()

from app.core import CharactersBot, ComicsBot, EventsBot


def sleep_hours(hours: int):
    time.sleep(60 * 60 * hours)


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
