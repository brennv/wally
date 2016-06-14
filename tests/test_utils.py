import pytest
from wally.utils import get_json
import json


def test_get_json():
    # url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    json = requests.get(url).json()
    assert get_json(url) == json

"""
def test_get_keys():
    domain = 'data.sfgov.org'
    # https://data.sfgov.org/api/catalog/v1?only=datasets
    keys = get_keys(domain)
    key = 'yitu-d5am'  # stateful
    assert key in keys

def test_get_metadata():
    url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    count_url = 'https://data.sfgov.org/api/views/yitu-d5am.json?$select=count(*)'
    metadata = requests.get(url).json()
    count = requests.get(count_url).json()

    # name, updated, rowCount, columnCount, columns, blurb
    pass
"""
