from app.bots.base import MarvelBot


class CharactersBot(MarvelBot):

    def get_random_character(self):
        marvel_character = self.marvel_api.get_random_character()

        if marvel_character.thumbnail.is_available():
            return marvel_character

        return self.get_random_character()

    def run(self):
        while True:
            marvel_character = self.get_random_character()
            tw_status = marvel_character.twitter_status

            self.logger.info(f'Tweet: {tw_status}')

            tw_status = self.twitter_api.update_with_media(
                status=tw_status,
                filename=marvel_character.thumbnail.name,
                file=marvel_character.thumbnail.image_data
            )

            self.wait_for_tweet()
