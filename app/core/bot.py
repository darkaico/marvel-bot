import random
import time
from datetime import datetime

import schedule

from app.core.jobs import CharactersJob, ComicsJob, EventsJob
from app.twitter.api import TwitterAPI
from app.telegram.api import TelegramAPI
from app.utils.mixins import LoggerMixin

HI_PHRASES = ["Holly Molly!", "Marvel movies time!", "Stay calm and assemble!"]


class MarvelBot(LoggerMixin):
    def start(self):
        self._say_hi()
        self._schedule_jobs()
        self._start_jobs()

    def _schedule_jobs(self):
        self.logger.info("Scheduling jobs")

        schedule.every().day.at("10:30").do(CharactersJob().execute)
        schedule.every().wednesday.at("13:15").do(ComicsJob().execute)
        schedule.every().friday.at("18:00").do(EventsJob().execute)

    def _start_jobs(self):
        self.logger.info("Starting jobs")
        while True:
            schedule.run_pending()
            time.sleep(1)

    def _say_hi(self):
        now = datetime.now()
        time_string = now.strftime("%H:%M")
        date_string = now.strftime("%d/%m/%Y")
        phrase = random.choice(HI_PHRASES)

        status = f"Wow {time_string} and today is {date_string}...\n\n{phrase}\n\n#wakingup"

        TwitterAPI.instance().update_status(status)
        TelegramAPI.instance().send_message(status)