from dataclasses import dataclass
from typing import Optional

from marvel_bot.utils import string_utils

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

    def build_twitter_status(self, title):
        status = f"{title}\n\n"
        status += f'Have you read "{self.title}"?\n'
        status += self.build_links_label()

        return status

    def build_telegram_status(self, title):
        status = f"*{title}*\n\n"
        status += f'Have you read "{self.title}"?\n'
        status += self.build_markdown_links()

        return status
