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
