import os

import tweepy
from dotenv import load_dotenv

from app.marvel import MarvelAPI

load_dotenv()

public_key = os.getenv("MARVEL_API_KEY")
private_key = os.getenv("MARVEL_PRIVATE_KEY")

marvel_api = MarvelAPI(public_key, private_key)

print(marvel_api.get_random_character())
