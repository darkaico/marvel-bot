

def test_marvel_api_hash(marvel_api_mock):

    assert isinstance(marvel_api_mock.generate_hash_token(1), str)


def test_marvel_ts_generation(marvel_api_mock):

    assert isinstance(marvel_api_mock.generate_ts(), float)


def test_same_hashes_same_ts_each_call(marvel_api_mock):
    ts = 47
    hash_one = marvel_api_mock.generate_hash_token(ts)
    hash_two = marvel_api_mock.generate_hash_token(ts)

    assert hash_one == hash_two


def test_different_hashes_different_ts_each_call(marvel_api_mock):
    ts_one = 47
    hash_one = marvel_api_mock.generate_hash_token(ts_one)

    ts_two = 74
    hash_two = marvel_api_mock.generate_hash_token(ts_two)

    assert hash_one != hash_two
