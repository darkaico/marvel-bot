import datetime

import factory
from factory.fuzzy import FuzzyChoice

from marvel_bot.marvel.constants import LinkTypeEnum
from marvel_bot.marvel.dtos import CharacterDTO, ComicDTO, EventDTO, ImageDTO
from marvel_bot.marvel.dtos.common_dto import MarvelLinkDTO


class MarvelLinkDTOFactory(factory.Factory):
    class Meta:
        model = MarvelLinkDTO

    type = FuzzyChoice(LinkTypeEnum)
    url = factory.Faker("url")


class ImageDTOFactory(factory.Factory):
    class Meta:
        model = ImageDTO

    path = factory.Faker("image_url")
    extension = factory.Faker("file_extension", category="image")


class ImageDTONoThumbnailFactory(ImageDTOFactory):
    path = "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available"


class MarvelResourceDTOFactory(factory.Factory):
    class Meta:
        abstract = True

    id = factory.Faker("pyint")
    thumbnail = factory.SubFactory(ImageDTOFactory)
    urls = factory.List([factory.SubFactory(MarvelLinkDTOFactory) for _ in range(5)])


class EventDTOFactory(MarvelResourceDTOFactory):
    class Meta:
        model = EventDTO

    title = factory.Faker("sentence", nb_words=4)
    start = factory.Faker(
        "date_between_dates",
        date_start=datetime.date(1983, 1, 1),
        date_end=datetime.date(1988, 5, 31),
    )
    end = factory.Faker(
        "date_between_dates",
        date_start=datetime.date(1990, 1, 1),
        date_end=datetime.date(2001, 5, 31),
    )
    description = factory.Faker("text")


class ComicDTOFactory(MarvelResourceDTOFactory):
    class Meta:
        model = ComicDTO

    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")


class CharacterDTOFactory(MarvelResourceDTOFactory):
    class Meta:
        model = CharacterDTO

    name = factory.Faker("first_name")
    comics = factory.SubFactory(ComicDTOFactory)
    description = factory.Faker("text")
