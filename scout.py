from config import db_uri
from integrations import slack
import os

from diff.soda import *  # TODO classy api methods


class Scout():
    ''''''
    def __init__(self, doc):
        print(doc)
        self.domain = doc['domain']
        self.name = doc['name']
        self.locale = doc['locale']
        self.webkooks = doc['webhooks']
        self.db_uri = db_uri
        self.db_table = doc['domain'].strip('.')
        # if doc['api']['kind'] == 'soda':
        #     from diff.soda import *

    def run(self):
        '''Check data collections and report changes.'''
        if os.path.isfile(self.db_uri):  # TODO refactor for postgres
            df1, df2, is_diff = check_diff(self)
            if is_diff:
                slack_note, twitter_note = get_notes(self, df1, df2)
                if slack_note:
                    response = slack(self, slack_note)
                    if response == 'ok':
                        set_db(self, df2)
                if twitter_note:
                    tweet(self, twitter_note)
                    print('tweet')
        else:
            df1 = get_df(self)
            set_db(self, df1)
        print('Done with...', self.domain)
        return True
