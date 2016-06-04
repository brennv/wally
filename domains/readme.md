### Configuring actions and attributes by domain

Configs for each domain to be checked are stored here and represented as separate yaml files.

Example yaml file for data.sfgov.org

    domain: data.sfgov.org
    name: DataSF
    apiFamily: soda
    apiVersion: v1
    apiToken: ""    <-- your api token
    apiDocs: "https://data.sfgov.org/developers"
    locale: San Francisco
    db: ./data/data.sfgov.org.db
    slackUrl: ""    <-- your incoming Slack webhook
