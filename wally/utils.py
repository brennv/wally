import requests
import time
import json
import dataset


def get_json(self, url):
    '''Ping endpoint and return json.'''
    sleep_time = 3600 / self.requestsPerHour
    try:
        json = requests.get(url).json()
    except BaseException as e:  # MaxRetryError
        print('error', e)
        # time.sleep(4000)
    time.sleep(sleep_time)
    return json

def theatrics(self):
    db_uri = self.db_uri
    domain = self.domain
    db = dataset.connect(db_uri)
    table = db.get_table(domain, primary_id='key', primary_type='String')
    # table = domain

    api_ids = request_ids()
    for _id in api_ids[0]:
        api_data = request_data(_id)
        record = table.find_one(key='_id')
        # db_data = search(data['key'])
        if not record:
            api_data['note'] = 'new dataset'
            ## cue_msg('new', api_data)
            # insert(api_data)
        if record and api_data != record:
            # diff data
            ## cue_msg('update')
            upsert(api_data)

    db_ids = get_ids()
    for _id in db_ids:
        if _id not in api_ids:
            ## cue_msg('removed')
            delete(_id)
    ## for msg in cue:
    ##     notify()
