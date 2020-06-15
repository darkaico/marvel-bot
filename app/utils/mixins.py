import logging


class LoggerMixin:

    _logger = None

    @property
    def logger(self):
        if not self._logger:
            log_name = self.__class__.__name__.lower()

            self._configure_logging(log_name)
            self._logger = logging.getLogger(log_name)

        return self._logger

    def _configure_logging(self, filename):
        logging.basicConfig(
            filename=f'{filename}.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
