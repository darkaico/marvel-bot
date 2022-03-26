from marvel_bot.utils import string_utils


def test_maximum():

    assert string_utils.limit_text("Hola Amigo", limit=5) == "Ho..."
