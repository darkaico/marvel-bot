import time

from dotenv import load_dotenv

from app.bots import (
    CharactersBot,
    ComicsBot,
    EventsBot
)

load_dotenv()


def start_bots():
    CharactersBot().start()

    time.sleep(60*60*2)
    ComicsBot().start()

    time.sleep(60*60*2)
    EventsBot().start()


def init():
    if __name__ == "__main__":
        start_bots()


init()
