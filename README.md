# data-scout

A pre-alpha tool for diff'ing metadata from open data APIs and sending notifications:
- new dataset added
- dataset updates (row counts)
- datasets removed

## Integrations

Data-scout is integrated with:
- Slack using [incoming webhooks](https://api.slack.com/incoming-webhooks)

## Getting started

    git clone ..
    cd data-scout
    python3 -m .env
    pip install -r requirements
    python run.py

### Configuring webhook actions

Webhooks for each api to be checked are represented as separate yaml files. Currently, only soda-based apis are supported.

Example yaml file for data.sfgov.org

    domain: data.sfgov.org
    name: DataSF
    locale: San Francisco
    api:
      kind: soda
      version: v1
      token: ""
    webhooks:
      slack:  
        url: ""

### Development

For dev/testing, domain metadata is housed in the data folder with sqlite
