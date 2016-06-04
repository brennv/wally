import os
import yaml


def get_docs(rel_dir):
    docs = []
    path = os.path.join(os.getcwd(), rel_dir)
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as stream:
                doc = yaml.load(stream)
                docs.append(doc)
    return docs

docs = get_docs('./_gists')
