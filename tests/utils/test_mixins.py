import logging

import pytest

from app.utils.mixins import LoggerMixin


class LoggerWithName(LoggerMixin):

    logger_name = 'ingenious'


class LoggerWithoutName(LoggerMixin):
    pass


@pytest.fixture
def class_with_logger_name():
    return LoggerWithName()


@pytest.fixture
def class_witout_logger_name():
    return LoggerWithoutName()


def test_logger_with_name_created(class_with_logger_name):

    assert isinstance(class_with_logger_name.logger, logging.Logger)


def test_logger_without_name_created(class_witout_logger_name):

    assert isinstance(class_witout_logger_name.logger, logging.Logger)
