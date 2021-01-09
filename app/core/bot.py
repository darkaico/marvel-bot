import time

import schedule

from app.core.jobs import CharactersJob, ComicsJob, EventsJob
from app.twitter.api import TwitterAPI
from app.utils.mixins import LoggerMixin


class MarvelBot(LoggerMixin):
    logger_name = "marvel_bot"

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
        TwitterAPI.instance().update_status("Saturday of marvel movies!")
