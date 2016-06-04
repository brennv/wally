# data-scout

A pre-alpha tool for diff'ing metadata from open data APIs and sending notifications:
- new dataset added
- dataset updates (row counts)
- datasets removed

## Getting started

  git clone ..
  cd data-scout
  python3 -m .env
  pip install -r requirements
  python run.py

### Configuring

Configs for domains to be checked are stored here and represented as separate yaml files.

Example yaml file for data.sfgov.org

  domain: data.sfgov.org
  name: DataSF
  apiFamily: soda
  apiVersion: v1
  apiToken: ""    <-- your api token
  apiDocs: "https://data.sfgov.org/developers"
  locale: San Francisco
  db: ./data/data.sfgov.org.db
  slackUrl: ""    <-- your [incoming Slack webhook](https://api.slack.com/incoming-webhooks)

### Development

For dev/testing, domain metadata is housed in the data folder with sqlite
