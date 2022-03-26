from io import BytesIO

import requests


def build_image_from_url(image_url):
    response = requests.get(image_url)

    return BytesIO(response.content)
