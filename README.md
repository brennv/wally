# wally

A pre-alpha tool to diff api results as well as:
- serve diff results via an api
- integrate notifications

![](http://s31.postimg.org/shsmoxv0r/wally.png)

## Integrations

- Slack using [incoming webhooks](https://api.slack.com/incoming-webhooks)

## Getting started

    make install
    # add api tokens and webhook urls to apis/
    make run

### Configuration

APIs to be diff'd are represented as separate yaml files in **apis/**.

    domain: data.sfgov.org
    name: DataSF
    locale: San Francisco
    api:
      kind: soda
      version: v1
      token: "your-api-token"
      hourlyLimit: 1000
    webhooks:
      - kind: slack
        url: "your-slack-webhook-url"

### Attributions

Image copyright 1997, Warner Bros.
