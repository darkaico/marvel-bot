import os

import tweepy

from marvel_bot.utils.singleton import SingletonMixin


class TwitterAPI(SingletonMixin):
    API_KEY = os.getenv("TW_API_KEY")
    SECRET_KEY = os.getenv("TW_SECRET_KEY")
    ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN")
    ACCESS_SECRET_TOKEN = os.getenv("TW_ACCESS_TOKEN_SECRET")

    def __init__(self):
        auth = tweepy.OAuthHandler(self.API_KEY, self.SECRET_KEY)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET_TOKEN)

        self.api = tweepy.API(auth)

    def update_status(self, status, in_reply_to_status_id=None):
        return self.api.update_status(
            status,
            in_reply_to_status_id=in_reply_to_status_id,
        )

    def update_with_media(self, status, filename, file, in_reply_to_status_id=None):

        return self.api.update_status_with_media(
            filename=filename,
            status=status,
            file=file,
            in_reply_to_status_id=in_reply_to_status_id,
        )

    def get_timeline(self):
        return self.api.user_timeline()

    def destroy_status(self, status_id):
        return self.api.destroy_status(status_id)
