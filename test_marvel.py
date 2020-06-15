import os

import requests
import tweepy
from dotenv import load_dotenv

from app.marvel.api import MarvelAPI

load_dotenv()

public_key = os.getenv("MARVEL_API_KEY")
private_key = os.getenv("MARVEL_PRIVATE_KEY")

marvel_api = MarvelAPI(public_key, private_key)

consumer_key = os.getenv("TW_API_KEY")
consumer_secret = os.getenv("TW_SECRET_KEY")

access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

character = marvel_api.get_random_character()

print(character.twitter_feed)
print(character.thumbnail.image_url)

r = requests.get(character.thumbnail.image_url, allow_redirects=True)
image = open(character.thumbnail.image_url, 'wb').write(r.content)

api.update_with_media(image, character.twitter_feed)
