from dataclasses import dataclass
from typing import List

from app.marvel.constants import LinkTypeEnum

from .common_dto import ImageDTO, MarvelLinkDTO


@dataclass
class MarvelResourceDTO:

    id: int
    thumbnail: ImageDTO
    urls: List[MarvelLinkDTO]

    _marvel_links_by_type = None

    def __post_init__(self):
        self._marvel_links_by_type = {}
        # Set marvel links by type if exists
        if self.urls:
            for marvel_link in self.urls:
                self._marvel_links_by_type[marvel_link.link_type] = marvel_link

    @property
    def detail_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.DETAIL)

    @property
    def wiki_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.WIKI)

    @property
    def comic_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.COMIC)

    @property
    def purchase_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.PURCHASE)

    @property
    def reader_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.READER)

    @property
    def in_app_link(self):
        return self._marvel_links_by_type.get(LinkTypeEnum.IN_APP_LINK)

    def build_links_label(self):
        links_label = ""

        if self.wiki_link:
            links_label += f"\n🔗 Wiki: {self.wiki_link.clean_url}"

        if self.detail_link:
            links_label += f"\n🔗 Details: {self.detail_link.clean_url}"

        if self.comic_link:
            links_label += f"\n🔗 Comics: {self.comic_link.clean_url}"

        if self.purchase_link:
            links_label += f"\n🔗 Purchase: {self.purchase_link.clean_url}"

        if self.reader_link:
            links_label += f"\n🔗 Reader: {self.reader_link.clean_url}"

        if self.in_app_link:
            links_label += f"\n🔗 In App Link: {self.in_app_link.clean_url}"

        return links_label

    def build_markdown_links(self):
        links_label = ""

        if self.wiki_link:
            links_label += f"\n🔗 [Wiki]({self.wiki_link.clean_url})"

        if self.detail_link:
            links_label += f"\n🔗 [Details]({self.detail_link.clean_url})"

        if self.comic_link:
            links_label += f"\n🔗 [Comics]({self.comic_link.clean_url})"

        if self.purchase_link:
            links_label += f"\n🔗 [Purchase]({self.purchase_link.clean_url})"

        if self.reader_link:
            links_label += f"\n🔗 [Reader]({self.reader_link.clean_url})"

        if self.in_app_link:
            links_label += f"\n🔗 [In App Link]({self.in_app_link.clean_url})"

        return links_label