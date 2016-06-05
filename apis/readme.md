### Configuring actions and attributes by domain

Configs for each domain to be checked are stored here and represented as separate yaml files.

Example yaml file for data.sfgov.org

    domain: data.sfgov.org
    name: DataSF
    locale: San Francisco
    api:
      kind: soda
      version: v1
      token: ""    <-- your domain api token
    webhooks:
      slack: ""    <-- your Slack webhook url
