import pytest
from wally.utils import get_json, get_docs, init_db
import requests
import json
from timeit import default_timer as timer


def test_get_json():
    # url = 'https://data.sfgov.org/api/views/yitu-d5am.json'
    url = 'http://jsonplaceholder.typicode.com/posts/1'
    json = requests.get(url).json()
    start = timer()
    expected = get_json(url, 1000)
    elapsed = timer() - start
    assert elapsed > 3.6
    assert expected == json

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


def test_get_docs():
    expected = [{'locale': None, 'domain': None, 'name': None, \
        'webhooks': [{'kind': None, 'url': ''}], \
        'api': {'hourlyLimit': None, 'kind': None, 'token': '', 'version': None}}]
    result = get_docs('tests/monitor/')
    assert result == expected

def test_init_db():
    pass
