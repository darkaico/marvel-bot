from dataclasses import dataclass
from typing import Optional

from app.utils import string_utils

from .base import MarvelResourceDTO


@dataclass
class CharacterComicDTO:

    available: int


@dataclass
class CharacterDTO(MarvelResourceDTO):

    name: str
    comics: CharacterComicDTO
    description: Optional[str] = None

    def __str__(self):
        return f"{self.id} - {self.name}"

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    def build_twitter_status(self, title):
        status = f"{title}\n\n"
        status += f"Did you know about {self.name} ?\n"
        status += self.build_links_label()

        return status

    def build_telegram_status(self, title):
        status = f"*{title}*\n\n"
        status += f"Did you know about {self.name} ?\n"
        status += self.build_markdown_links()

        return status
