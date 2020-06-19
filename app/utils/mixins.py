import logging
import os

from app import BASE_DIR


class LoggerMixin:

    _logger = None
    logger_name = None

    @property
    def logger(self):
        if not self._logger:
            logger_name = self.logger_name
            if not logger_name:
                logger_name = self.__class__.__name__.lower()

            self._logger = build_logger(logger_name)

        return self._logger


def build_logger(logger_name):
    """Create and configure a default financial tool logger."""
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    log_filename = f'{BASE_DIR}/logs/{logger_name}.log'
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)

    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)

    return logger
