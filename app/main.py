from dotenv import load_dotenv

load_dotenv()


def init():
    if __name__ == "__main__":
        from app.core.bot import MarvelBot

        MarvelBot().run()


init()
