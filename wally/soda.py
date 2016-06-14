# from spencer.diff import *
# from spencer.integrations import slack
from wally.utils import get_json, diff
import dataset
import os


class Soda():
    def __init__(self, doc, db_uri):
        # def soda(doc, db_uri):
        '''Check data collections and report changes.'''
        self.domain = doc['domain']
        self.name = doc['name']
        self.locale = doc['locale']
        self.resource = doc['resource']
        self.webhooks = doc['webhooks']
        self.db_table = doc['domain']
        self.db_uri = db_uri
        self.requestsPerHour = 1000

    def request_ids(self):
        '''Get the ids of all the datasets in the domain catalog.'''
        domain = self.domain
        endpoint = '/api/catalog/v1?only=datasets'  # self.resource.url
        catalog_url = 'https://' + domain + endpoint
        tail = "&offset="
        size = "resultSetSize"
        catalog = get_json(self, catalog_url)
        uids = [x['resource']['id'] for x in catalog['results']]
        resultCount = catalog[size]
        setSize = len(uids)
        pages = resultCount // setSize + (resultCount % setSize > 0)
        offset = 0
        for page in range(1, pages):
            offset += setSize
            url = catalog_url + tail + str(offset)
            catalog = get_json(self, url)
            pageUids = [x['resource']['id'] for x in catalog['results']]
            uids = uids + pageUids
        return uids

    def request_data(self, uid):
        '''Get metdata for a given dataset unique id.'''
        domain = self.domain
        data = {'key': uid}
        ### 1st endpoint
        url = 'https://' + domain + '/api/views/ '+ uid + ".json"
        view = get_json(self, url)
        fields = ["name", "rowsUpdatedAt", "description"]
        # updated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(views['rowsUpdatedAt']))
        # columns = [x['name'] for x in views['columns']]
        # columnCount = len(columns)
        for field in fields:
            try:
                data[field] = view[field]
            except KeyError as e:
                data[field] = None
        ### 2nd endpoint
        url = 'https://' + domain + "/resource/" + uid + ".json?$select=count(*)"
        view = get_json(self, url)
        view = view[0]
        fields = ['count']
        for field in fields:
            try:
                data[field] = view[field]
            except KeyError as e:
                data[field] = None
        return data

        print('Done with...', self.domain)
        return True

    def run(self):
        diff(self)
        return True
