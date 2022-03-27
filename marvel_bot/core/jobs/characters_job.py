from marvel_bot.marvel.dtos.character_dto import CharacterDTO

from .base import MarvelJob


class CharactersJob(MarvelJob):
    def get_title(self):
        return "🎉🎉🎉 Weekly Event 🎉🎉🎉"

    def get_resource(self) -> CharacterDTO:
        return self.marvel_api.get_random_character()
