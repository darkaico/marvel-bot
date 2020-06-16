from dataclasses import dataclass
from typing import Optional

from app.utils import string_utils

from .common_dto import ImageDTO


@dataclass
class CharacterComicDTO:

    available: int


@dataclass
class CharacterDTO:

    id: int
    name: str
    thumbnail: ImageDTO
    comics: CharacterComicDTO
    description: Optional[str] = None

    def __str__(self):
        return f'{self.id} - {self.name}'

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    @property
    def twitter_status(self):
        status = f'Did you know about {self.name} ?'
        if self.description:
            status += f'\n{self.short_description}'

        return status

    @property
    def twitter_summary(self):
        summary = f'* Available in:\n'
        summary *= f'* {self.comics.available} comics.\n'
        summary *= f'* {self.comics.available} series.\n'

        return summary
