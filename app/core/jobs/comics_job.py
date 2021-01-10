from .base import MarvelJob


class ComicsJob(MarvelJob):
    def _get_random_comic(self):
        marvel_comic = self.marvel_api.get_random_comic()
        if marvel_comic.thumbnail.is_available():
            return marvel_comic

        return self._get_random_comic()

    def execute(self):
        marvel_comic = self._get_random_comic()

        tw_status = "🎉🎉🎉 Weekly Comic 🎉🎉🎉\n"
        tw_status += "#marvel #comicoftheday\n\n"
        tw_status += marvel_comic.twitter_status

        self.logger.info(f"Tweet: {tw_status}")

        self.twitter_api.update_with_media(
            status=tw_status,
            filename=marvel_comic.thumbnail.name,
            file=marvel_comic.thumbnail.image_data,
        )
