# data-scout

A pre-alpha tool for diff'ing metadata from open data APIs and sending notifications:
- new datasets added
- dataset updates (row counts)
- datasets removed

## Integrations

- Slack using [incoming webhooks](https://api.slack.com/incoming-webhooks)

## Getting started

    make install
    # add api tokens and webhook urls to apis/
    make run

### Configuring webhooks

Webhooks for each api are represented as separate yaml files in **apis/**.

    domain: data.sfgov.org
    name: DataSF
    locale: San Francisco
    api:
      kind: soda
      version: v1
      token: "your-api-token"
    webhooks:
      - kind: slack
        url: "your-slack-webhook-url"
