from marvel_bot.utils.logger_utils import build_logger


class LoggerMixin:

    _logger = None
    logger_name = None

    @property
    def logger(self):
        if not self._logger:
            logger_name = self.logger_name or "marvel_bot"
            if not logger_name:
                logger_name = self.__class__.__name__.lower()

            self._logger = build_logger(logger_name)

        return self._logger
