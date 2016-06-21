import os
import yaml
import requests
import time
import json
import dataset
import pyorient


def get_json(url, rate):
    '''Ping endpoint and return json.'''
    sleep_time = 3600 / rate
    try:
        json = requests.get(url).json()
    except BaseException as e:  # MaxRetryError
        print('error', e)
        # time.sleep(4000)
    time.sleep(sleep_time)
    return json

def get_domains(rel_dir):
    url = 'http://api.us.socrata.com/api/catalog/v1/domains?only=datasets'
    results = requests.get(url).json()['results']
    for result in results:
        domain = result['domain']
        count = result['count']
        file_name = domain + '.yaml'
        file_path = os.path.join(os.getcwd(), rel_dir, file_name)
        if not os.path.isfile(file_path):
            dummy_file = os.path.join(os.getcwd(), rel_dir, '_dummy.yaml')
            with open(dummy_file, "r") as stream:
                doc = yaml.load(stream)
                doc['domain'] = domain

def get_docs(rel_dir):
    '''Load yaml files for each Scout instance.'''
    # TODO validation
    print('Getting domain configs...', rel_dir)
    docs = []
    path = os.path.join(os.getcwd(), rel_dir)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as stream:
                    doc = yaml.load(stream)
                    docs.append(doc)
    return docs

# docs = get_docs('./_gists')

def init_db():
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect( "admin", "admin" )
    db_uri = # self.db_uri
    domain = # self.domain
    db = dataset.connect(db_uri)
    table = db.get_table(domain, primary_id='key', primary_type='String')
    # table = domain

def check_diff_adds():
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

def check_diff_dels():
    db_ids = get_ids()
    for _id in db_ids:
        if _id not in api_ids:
            ## cue_msg('removed')
            delete(_id)
    ## for msg in cue:
    ##     notify()
