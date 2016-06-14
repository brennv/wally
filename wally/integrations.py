import slackweb


def slack(url, note):
    '''Send message to slack channel.'''
    response = 'null'
    if note != []:
        print('Slacking update...')
        post = slackweb.Slack(url=url)
        response = post.notify(text=note)
    return response

def tweet(self, note):
    pass

def sms(self, note):
    pass

def email(self, note):
    pass

# slack_note, twitter_note = get_notes(self.domain, df1, df2)
# response = ''
# for hook in self.webhooks:
#     if hook['kind'] == 'slack' and len(slack_note) > 10:  # not None
#         url = hook['url']
#         response = slack(url, slack_note)
    # if hook['kind'] == 'twitter' and len(twitter_note) > 10:  # not None
    #     url = hook['url']
    #     response = slack(url, twitter_note)
# if response == 'ok':
