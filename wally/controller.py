import os
import yaml
import requests


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

docs = get_docs('./_gists')
