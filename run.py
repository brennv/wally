from controller import docs
from config import db_uri
from diff.soda import Soda


def main():
    for doc in docs:
        print(doc)
        if doc['api']['kind'] == 'soda':
            scout = Soda(doc, db_uri)
            scout.run()

if __name__ == '__main__':
    main()
