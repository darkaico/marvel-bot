from .base import MarvelJob


class EventsJob(MarvelJob):
    def execute(self):
        marvel_event = self.marvel_api.get_random_event()

        title = "🎉🎉🎉 Weekly Event 🎉🎉🎉\n"
        tw_status = marvel_event.build_twitter_status(title)
        telegram_status = marvel_event.build_telegram_status(title)

        self.logger.info(f"Tweet: {tw_status}")
        self.logger.info(f"Telegram: {telegram_status}")

        self.twitter_api.update_with_media(
            status=tw_status,
            filename=marvel_event.thumbnail.name,
            file=marvel_event.thumbnail.image_data,
        )

        self.telegram_api.send_message(telegram_status)
