from dotenv import load_dotenv

from app.bots.character_bot import CharacterBot

load_dotenv()


if __name__ == "__main__":
    CharacterBot().start()
