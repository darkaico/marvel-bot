from dataclasses import dataclass
from io import BytesIO

import requests


@dataclass
class ImageDTO:

    path: str
    extension: str

    @property
    def url(self):
        return f'{self.path}.{self.extension}'

    @property
    def name(self):
        return self.url.rsplit('/', 1)[1]

    @property
    def image_data(self):
        response = requests.get(self.url)

        return BytesIO(response.content)


@dataclass
class CharacterDTO:

    id: int
    name: str
    description: str
    thumbnail: ImageDTO

    @property
    def short_description(self):
        return (self.description[:100] + '..') if len(self.description) > 100 else self.description

    @property
    def twitter_status(self):
        status = f'Did you know about {self.name} ?'
        if self.description:
            status += f'\n{self.short_description}'

        return status
