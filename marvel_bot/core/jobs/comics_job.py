from marvel_bot.marvel.dtos.comic_dto import ComicDTO

from .base import MarvelJob


class ComicsJob(MarvelJob):
    def get_title(self):
        return "🎉🎉🎉 Comic of the week 🎉🎉🎉"

    def get_resource(self) -> ComicDTO:
        return self.marvel_api.get_random_comic()
