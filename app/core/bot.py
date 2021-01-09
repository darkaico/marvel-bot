import time

import schedule

from app.core.jobs.characters_job import CharacterJob
from app.core.jobs.comics_job import ComicsJob
from app.core.jobs.events_job import EventsJob


class MarvelBot:
    def __init__(self):
        schedule.every().day.at("10:30").do(CharacterJob().execute)
        schedule.every().wednesday.at("13:15").do(ComicsJob().execute)
        schedule.every().friday.at("18:00").do(EventsJob().execute)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
