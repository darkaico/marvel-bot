import requests
import os

from app.utils.singleton import SingletonMixin


class TelegramConnectionException(Exception):
    pass


class TelegramApi(SingletonMixin):
    BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    DEFAULT_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    @property
    def base_url(self):
        return f"https://api.telegram.org/bot{self.BOT_TOKEN}"

    def send_message(self, message: str, chat_id: str = None):
        if not chat_id:
            chat_id = self.DEFAULT_CHAT_ID

        params = {"chat_id": chat_id, "parse_mode": "Markdown", "text": message}
        response = requests.get(f"{self.base_url}/sendMessage", params=params)

        if response.status_code != 200:
            raise TelegramConnectionException(response)

        return response.json()

    def send_media(self, file_path: str, chat_id: str = None):
        if not chat_id:
            chat_id = self.DEFAULT_CHAT_ID

        with open(file_path, "rb") as img:
            file_absolute_path = os.path.basename(file_path)
            files = {
                "document": (
                    file_absolute_path,
                    img,
                    "multipart/form-data",
                    {"Expires": "0"},
                )
            }
            with requests.Session() as s:
                response = s.post(
                    f"{self.base_url}/sendDocument", data={"chat_id": chat_id}, files=files
                )

            if response.status_code != 200:
                raise TelegramConnectionException(response)