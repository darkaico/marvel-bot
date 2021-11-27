import pytest
import requests

from app.telegram.api import TelegramAPI, TelegramConnectionException
from tests.conftest import MockResponse


@pytest.fixture
def telegram_api_mock():
    return TelegramAPI.instance()


def test_telegram_base_url(telegram_api_mock):

    assert telegram_api_mock.base_url.startswith("https://api.telegram.org/bot")


def test_telegram_custom_exception(telegram_api_mock, monkeypatch):
    monkeypatch.setattr(requests, "get", lambda url, params: MockResponse(status_code=400))

    with pytest.raises(TelegramConnectionException):
        telegram_api_mock.send_message("things are not going well")


def test_send_message_default_chat_id(telegram_api_mock, mocker):
    mocker.patch.object(requests, "get", return_value=MockResponse(status_code=200))

    telegram_api_mock.send_message("marvelouso")

    expected_url = f"{telegram_api_mock.base_url}/sendMessage"
    expected_params = {
        "chat_id": telegram_api_mock.DEFAULT_CHAT_ID,
        "parse_mode": "Markdown",
        "text": "marvelouso",
    }
    requests.get.assert_called_with(expected_url, params=expected_params)


def test_send_message_explicit_chat_id(telegram_api_mock, mocker):
    mocker.patch.object(requests, "get", return_value=MockResponse(status_code=200))

    telegram_api_mock.send_message("que tal?", "CHAT78")

    expected_url = f"{telegram_api_mock.base_url}/sendMessage"
    expected_params = {
        "chat_id": "CHAT78",
        "parse_mode": "Markdown",
        "text": "que tal?",
    }
    requests.get.assert_called_with(expected_url, params=expected_params)
