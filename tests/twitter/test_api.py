

def test_get_timeline(twitter_api_mock):

    assert isinstance(twitter_api_mock.get_timeline(), list)


def test_api_update_status(twitter_api_mock):
    status = 'Hola amigos'

    assert twitter_api_mock.update_status(status).text == 'Hola amigos'


def test_api_update_with_media(twitter_api_mock):
    status = 'Twitt with media'

    assert twitter_api_mock.update_with_media(
        status=status,
        filename='',
        file=None
    ).text == status


def test_api_destroy_status(twitter_api_mock):

    assert twitter_api_mock.destroy_status(2).id == 2
