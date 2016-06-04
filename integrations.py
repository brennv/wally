import slackweb


def notify_slack(self, note):
    '''Send message to slack channel.'''
    response = 'null'
    if note != []:
        print('Slacking update...')
        slack = slackweb.Slack(url=self.slackUrl)
        response = slack.notify(text=note)
    return response
