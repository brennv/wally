from integrations import notify_slack
from diff.soda import *
import os


class Scout():
    def __init__(self, doc):
        print(doc)
        self.domain = doc['domain']
        self.name = doc['name']
        self.apiFamily = doc['apiFamily']
        self.apiVersion = doc['apiVersion']
        self.apiToken = doc['apiToken']
        self.apiDocs = doc['apiDocs']
        self.locale = doc['locale']
        self.db = doc['db']
        self.slackUrl = doc['slackUrl']

    def run(self):
        '''Check data collections and report changes.'''
        if os.path.isfile(self.db):
            df1, df2, is_diff = check_diff(self)
            if is_diff:
                slack_note, twitter_note = get_notes(self, df1, df2)
                if slack_note:
                    response = notify_slack(self, slack_note)
                    if response == 'ok':
                        set_db(self, df2)
                if twitter_note:
                    print('tweet')
        else:
            df1 = get_df(self)
            set_db(self, df1)
        print('Done with...', self.domain)
        return True
