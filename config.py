import os


env = os.getenv('ENV') or 'DEV'

if env == 'DEV':
    api_dir = './webhooks'
    db_uri = 'sqlite:///data/data.db'

if env == 'TEST':
    api_dir = './webhooks'
    db_uri = ''

if env == 'PROD':
    api_dir = './webhooks'
    db_uri = ''
