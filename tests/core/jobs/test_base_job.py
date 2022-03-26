import pytest

from marvel_bot.core.jobs.base import MarvelJob


@pytest.fixture
def mock_marvel_job():
    return MarvelJob()


def test_execute_should_be_implemented(mock_marvel_job):
    with pytest.raises(NotImplementedError):
        mock_marvel_job.execute()


def test_weekday(mock_marvel_job):

    assert isinstance(mock_marvel_job.weekday, str)
