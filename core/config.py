import os


env = os.getenv('ENV') or 'DEV'

if env == 'DEV':
    db_uri = 'sqlite:///data.db'

if env == 'TEST':
    db_uri = ''

if env == 'PROD':
    db_uri = ''
