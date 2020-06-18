from dataclasses import dataclass
from typing import Optional

from app.utils import string_utils

from .base import MarvelResourceDTO
from .common_dto import ImageDTO


@dataclass
class ComicDTO(MarvelResourceDTO):

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
