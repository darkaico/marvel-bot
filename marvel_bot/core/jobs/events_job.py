from marvel_bot.marvel.dtos.event_dto import EventDTO

from .base import MarvelJob


class EventsJob(MarvelJob):
    def get_title(self):
        return "🧩🧩🧩 Event of the Week 🧩🧩🧩"

    def get_resource(self) -> EventDTO:
        return self.marvel_api.get_random_event()
