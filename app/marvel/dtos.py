from dataclasses import dataclass


@dataclass
class ImageDTO:

    path: str
    extension: str

    @property
    def image_url(self):
        return f'{self.path}.{self.extension}'

@dataclass
class CharacterDTO:
    id: int
    name: str
    description: str
    thumbnail: ImageDTO

    @property
    def twitter_feed(self):
        return f"""Did you know about {self.name} ?\n
Something about: {self.description}
"""
