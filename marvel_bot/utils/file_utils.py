import os
from io import BytesIO

import requests


def build_image_from_url(image_url: str) -> BytesIO:
    if os.environ["ENV"] == "TEST":
        return BytesIO()

    response = requests.get(image_url)

    return BytesIO(response.content)
