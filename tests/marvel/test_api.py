

def test_marvel_api_hash(marvel_api_mock):

    assert isinstance(marvel_api_mock.hash, str)
