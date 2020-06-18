from app.bots.base import MarvelBot


class EventsBot(MarvelBot):

    tweet_interval = 24

    def get_random_event(self):
        marvel_event = self.marvel_api.get_random_event()
        if marvel_event.thumbnail.is_available():
            return marvel_event

        return self.get_random_event()

    def run(self):
        while True:
            marvel_event = self.get_random_event()

            self.logger.info(f'Tweeting about: {marvel_event}')

            tw_status = f'=== {self.weekday} Event ===\n'
            tw_status += f'#marvel #eventoftheday\n\n'
            tw_status += marvel_event.twitter_status

            self.logger.info(tw_status)

            self.twitter_api.update_with_media(
                status=tw_status,
                filename=marvel_event.thumbnail.name,
                file=marvel_event.thumbnail.image_data
            )

            self.wait_for_tweet()
