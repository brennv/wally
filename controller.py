from config import api_dir
import os
import yaml
# from apscheduler.scheduler import Scheduler


def get_specs(rel_dir):
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

apis = get_specs(api_dir)
