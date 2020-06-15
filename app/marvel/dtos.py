from dataclasses import dataclass
from io import BytesIO

import requests


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
        response = requests.get(self.url)

        return BytesIO(response.content)


@dataclass
class CharacterDTO:

    id: int
    name: str
    description: str
    thumbnail: ImageDTO

    def __str__(self):
        return f'{self.id} - {self.name}'

    @property
    def short_description(self):
        return (self.description[:200] + '..') if len(self.description) > 200 else self.description

    @property
    def twitter_status(self):
        status = f'Did you know about {self.name} ?'
        if self.description:
            status += f'\n{self.short_description}'

        return status
