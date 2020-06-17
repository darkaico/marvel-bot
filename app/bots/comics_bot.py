from app.bots.base import MarvelBot


class ComicsBot(MarvelBot):

    def get_comic(self):
        marvel_comic = self.marvel_api.get_random_character()
        if marvel_comic.thumbnail.is_available():
            return marvel_comic

        return self.get_comic()

    def run(self):
        while True:
            marvel_comic = self.get_comic()

            self.logger.info(f'Tweeting about: {marvel_comic}')

            tw_status = self.twitter_api.update_with_media(
                status=marvel_comic.twitter_status,
                filename=marvel_comic.thumbnail.name,
                file=marvel_comic.thumbnail.image_data
            )

            self.wait_for_tweet()
