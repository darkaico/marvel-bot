from dataclasses import dataclass

from app.marvel.constants import LinkTypeEnum
from app.utils import file_utils


@dataclass
class ImageDTO:

    path: str
    extension: str

    def is_available(self):
        return "image_not_available" not in self.name

    @property
    def url(self):
        return f"{self.path}.{self.extension}"

    @property
    def name(self):
        return self.url.rsplit("/", 1)[1]

    @property
    def image_data(self):
        return file_utils.build_image_from_url(self.url)


@dataclass
class MarvelLinkDTO:

    type: str
    url: str

    @property
    def link_type(self):
        return LinkTypeEnum(self.type)
