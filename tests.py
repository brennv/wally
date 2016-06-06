from diff.diff import get_json


def test_get_json():
    json = {}
    url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    assert get_json(url) == json
