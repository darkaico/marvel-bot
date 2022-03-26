from sentry_sdk import capture_message

from marvel_bot.core.bot import MarvelBot


def start_bot():

    MarvelBot().start()


def init():
    if __name__ == "__main__":
        capture_message("Starting the Marvel Bot", level="info")

        start_bot()


init()
