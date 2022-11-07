import os

import tweepy

from marvel_bot.utils.singleton import SingletonMixin

API_KEY = os.getenv("TW_API_KEY", "")
SECRET_KEY = os.getenv("TW_SECRET_KEY", "")
ACCESS_TOKEN = os.getenv("TW_ACCESS_TOKEN", "")
ACCESS_SECRET_TOKEN = os.getenv("TW_ACCESS_TOKEN_SECRET", "")


class TwitterAPI(SingletonMixin):
    def __init__(
        self,
        api_key: str = None,
        api_secret_key: str = None,
        access_token: str = None,
        access_secret_token: str = None,
    ):
        auth = tweepy.OAuthHandler(api_key or API_KEY, api_secret_key or SECRET_KEY)
        auth.set_access_token(
            access_token or ACCESS_TOKEN,
            access_secret_token or ACCESS_SECRET_TOKEN,
        )

        self.api = tweepy.API(auth)

    def update_status(self, status, in_reply_to_status_id=None):
        return self.api.update_status(
            status,
            in_reply_to_status_id=in_reply_to_status_id,
        )

    def update_status_with_media(self, status, filename, file, in_reply_to_status_id=None):

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
