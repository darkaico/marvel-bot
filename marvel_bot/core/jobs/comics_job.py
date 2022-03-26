from .base import MarvelJob


class ComicsJob(MarvelJob):
    def execute(self):
        marvel_comic = self.marvel_api.get_random_comic()

        title = "🎉🎉🎉 Weekly Comic 🎉🎉🎉"
        tw_status = marvel_comic.build_twitter_status(title)
        telegram_status = marvel_comic.build_telegram_status(title)

        self.logger.info(f"Tweet: {tw_status}")
        self.logger.info(f"Telegram: {telegram_status}")

        self.twitter_api.update_with_media(
            status=tw_status,
            filename=marvel_comic.thumbnail.name,
            file=marvel_comic.thumbnail.image_data,
        )

        self.telegram_api.send_message(telegram_status)
