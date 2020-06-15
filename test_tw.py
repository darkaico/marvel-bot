import os

import tweepy
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv("TW_API_KEY")
consumer_secret = os.getenv("TW_SECRET_KEY")

access_token = os.getenv("TW_ACCESS_TOKEN")
access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count=10)
for tweet in public_tweets:
    print(tweet.text)


api.update_status('Hola Mundillo')
