from dataclasses import dataclass
from typing import Optional

from app.utils import string_utils

from .base import MarvelResourceDTO


@dataclass
class ComicDTO(MarvelResourceDTO):

    title: str
    description: Optional[str] = None

    def __str__(self):
        return f"{self.id} - {self.title}"

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    @property
    def twitter_status(self):
        status = f'Have you read "{self.title}"?\n'
        status += self.build_links_label()

        return status
