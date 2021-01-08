import time

import pytest

from app.bots.base import MarvelBot


@pytest.fixture
def mock_marvel_bot():
    return MarvelBot()


def test_tweet_should_be_implemented(mock_marvel_bot):
    with pytest.raises(NotImplementedError):
        mock_marvel_bot.tweet()


def test_tweet_time(mock_marvel_bot):

    assert isinstance(mock_marvel_bot.generate_tweet_time(), int)


def test_tweet_time_differents(mock_marvel_bot):
    tweet_time_one = (mock_marvel_bot.generate_tweet_time(),)
    tweet_time_two = (mock_marvel_bot.generate_tweet_time(),)

    assert tweet_time_one != tweet_time_two


def test_weekday(mock_marvel_bot):

    assert isinstance(mock_marvel_bot.weekday, str)


def test_tweet_time(mock_marvel_bot, mocker):
    mocker.patch("time.sleep")

    mock_marvel_bot.wait_for_tweet()

    time.sleep.assert_called_once()
