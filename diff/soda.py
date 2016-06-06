from diff.diff import *
from integrations import slack
import os


class Soda():
    def __init__(self, doc, db_uri):
        # def soda(doc, db_uri):
        '''Check data collections and report changes.'''
        self.domain = doc['domain']
        self.name = doc['name']
        self.locale = doc['locale']
        self.webhooks = doc['webhooks']
        self.db_table = doc['domain'].strip('.')
        self.db_uri = db_uri

    def run(self):
        if os.path.isfile(self.db_uri):  # TODO refactor for postgres
            df1, df2, is_diff = check_diff(self.db_uri, self.db_table, self.domain)
            if is_diff:
                slack_note, twitter_note = get_notes(self.domain, df1, df2)
                if slack_note:
                    response = slack(self.webhooks.slack.url, slack_note)
                    if response == 'ok':
                        set_db(self.db_uri, self.db_table, df2)  # TODO cue messages
                # if twitter_note:
                #     tweet(webhooks.twitter.url, twitter_note)
                #     print('tweet')
        else:
            df1 = get_df(self.domain)
            set_db(self.db_uri, self.db_table, df1)
        print('Done with...', self.domain)
        return True
