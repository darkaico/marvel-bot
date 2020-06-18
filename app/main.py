import time

from dotenv import load_dotenv

from app.bots import (
    CharactersBot,
    EventsBot
)

load_dotenv()


def start_bots():
    EventsBot().start()

    time.sleep(60*60*4)

    CharactersBot().start()


def init():
    if __name__ == "__main__":
        start_bots()


init()
