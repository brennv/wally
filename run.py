from controller import docs
from config import db_uri
from diff.soda import Soda

def main():
    for doc in docs:
        if doc['api']['kind'] == 'soda':
            soda = Soda(doc, db_uri)
            soda.run()

if __name__ == '__main__':
    main()
