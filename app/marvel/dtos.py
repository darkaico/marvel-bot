from dataclasses import dataclass
from typing import Optional

from app.utils import (
    file_utils,
    string_utils
)


@dataclass
class ImageDTO:

    path: str
    extension: str

    def is_available(self):
        return 'image_not_available' not in self.name

    @property
    def url(self):
        return f'{self.path}.{self.extension}'

    @property
    def name(self):
        return self.url.rsplit('/', 1)[1]

    @property
    def image_data(self):
        return file_utils.build_image_from_url(self.url)


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


@dataclass
class ComicDTO:

    id: int
    title: str
    thumbnail: ImageDTO
    description: Optional[str] = None

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    @property
    def twitter_status(self):
        status = f'{self.title}'
        if self.description:
            status += f'\n{self.short_description}'

        return status
