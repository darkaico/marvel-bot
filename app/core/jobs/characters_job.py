from .base import MarvelJob


class CharactersJob(MarvelJob):
    def execute(self):
        marvel_character = self.marvel_api.get_random_character()

        title = f"🎉🎉🎉 {self.weekday} Character 🎉🎉🎉"
        tw_status = marvel_character.build_twitter_status(title)
        telegram_status = marvel_character.build_telegram_status(title)

        self.logger.info(f"Tweet: {tw_status}")
        self.logger.info(f"Telegram: {telegram_status}")

        self.twitter_api.update_with_media(
            status=tw_status,
            filename=marvel_character.thumbnail.name,
            file=marvel_character.thumbnail.image_data,
        )

        self.telegram_api.send_message(telegram_status)
