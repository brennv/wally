from wally.controller import docs
from wally.soda import Soda
from config import db_uri


def main():
    for doc in docs:
        print(doc)
        if doc['api']['kind'] == 'soda':
            wally = Soda(doc, db_uri)
            wally.run()

if __name__ == '__main__':
    main()
