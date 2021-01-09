from app.bots.base import MarvelBot


class EventsBot(MarvelBot):

    # Every 7 days
    tweet_interval = 60 * 60 * 24 * 7

    def _get_random_event(self):
        marvel_event = self.marvel_api.get_random_event()
        if marvel_event.thumbnail.is_available():
            return marvel_event

        return self._get_random_event()

    def tweet(self):
        marvel_event = self._get_random_event()

        tw_status = "🎉🎉🎉 Weekly Event 🎉🎉🎉\n"
        tw_status += "#marvel #eventoftheweek\n\n"
        tw_status += marvel_event.twitter_status

        self.logger.info(f"Tweet: {tw_status}")

        self.twitter_api.update_with_media(
            status=tw_status,
            filename=marvel_event.thumbnail.name,
            file=marvel_event.thumbnail.image_data,
        )
