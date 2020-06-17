from dataclasses import dataclass
from datetime import datetime
from typing import (
    List,
    Optional
)

from app.marvel.constants import LinkTypeEnum
from app.utils import string_utils

from .common_dto import (
    ImageDTO,
    MarvelLinkDTO
)


@dataclass
class EventDTO:

    _marvel_links_by_type = {}

    id: int
    title: str
    thumbnail: ImageDTO
    urls: Optional[List[MarvelLinkDTO]]
    start: Optional[datetime]
    end: Optional[datetime]
    description: Optional[str] = None

    def __post_init__(self):
        # Set marvel links by type
        for marvel_link in self.urls:
            self._marvel_links_by_type[marvel_link.link_type] = marvel_link

    def __str__(self):
        return f'{self.id} - {self.title}'

    @property
    def short_description(self):
        return string_utils.limit_text(self.description)

    @property
    def twitter_status(self):
        status = f'What do you know about "{self.title}" ?\n'

        if self.wiki_link:
            status += f'\n* Wiki: {self.wiki_link.url}'

        if self.detail_link:
            status += f'\n* Details: {self.detail_link.url}'

        if self.comic_link:
            status += f'\n* Comics: {self.comic_link.url}'

        return status

    @property
    def detail_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.DETAIL)

    @property
    def wiki_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.WIKI)

    @property
    def comic_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.COMIC)
