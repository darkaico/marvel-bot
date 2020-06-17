import tweepy


class TwitterAPI:

    def __init__(
        self,
        consumer_api_key,
        consumer_api_secret_key,
        access_token,
        access_token_secret,
    ):
        auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def update_status(self, status, in_reply_to_status_id=None):
        return self.api.update_status(
            status,
            in_reply_to_status_id=in_reply_to_status_id,
        )

    def update_with_media(self, status, filename, file, in_reply_to_status_id=None):

        return self.api.update_with_media(
            filename=filename,
            status=status,
            file=file,
            in_reply_to_status_id=in_reply_to_status_id
        )

    def get_timeline(self):
        return self.api.user_timeline()

    def destroy_status(self, status_id):
        return self.api.destroy_status(status_id)
