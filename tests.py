from diff.diff import get_json, get_keys, get_metadata
import requests
import json


def test_get_json():
    # url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    json = \
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    assert get_json(url) == json

def test_get_keys():
    domain = 'data.sfgov.org'
    # https://data.sfgov.org/api/catalog/v1?only=datasets
    keys = get_keys(domain)
    key = 'yitu-d5am'  # stateful
    assert key in keys

def test_get_metadata():
    url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    json = requests.get(url).json()
    # name, updated, rowCount, columnCount, columns, blurb
    pass
