import time

from dotenv import load_dotenv

from app.bots import (
    CharactersBot,
    EventsBot
)

load_dotenv()


if __name__ == "__main__":
    EventsBot().start()

    time.sleep(60*60*4)

    # CharactersBot().start()
