[![webhook-tester](https://github.com/leondelaimy/webhook-tester/actions/workflows/python-test.yml/badge.svg)](https://github.com/leondelaimy/webhook-tester/actions/workflows/python-test.yml)

<h1 align="center">
  Webhook Tester
</h1>
<p align="center">
  Receive, queue & process GitHub webhooks
</p>


<br/>

## Dependencies
- Docker
- VSCode devcontainer
- GitHub

<br/>

## Prerequisites

1. Set up an issue_comment webhook via GitHub UI pointing to the localtunnel endpoint

Payload URL: https://webhook-receiver.loca.lt \
Content type: application/json \
Create a secret for webhook verification

2. Update secrets in .devcontainer/devcontainer.env
```
GITHUB_WEBHOOK_TOKEN=<enter secret>
GITHUB_ACCESS_TOKEN=<enter secret>
```
3. Start up devcontainer in VSCode

<br/>

## Running services within devcontainer

1. Start development environment
```
make up
```
2. Run queue worker to process received webhooks
```
rq worker
```
3. Commit changes & create a pull request
4. Add a comment to trigger a merge request
```
#merge
```

<br/>

## Tools
https://github.com/microsoft/vscode-dev-containers \
https://github.com/jakbin/flask-localtunnel \
https://github.com/localtunnel/localtunnel \
https://github.com/lscsoft/webhook-queue \
https://github.com/rq/rq 

## Articles
https://hookdeck.com/webhooks/platforms/guide-github-webhooks-features-and-best-practices \
https://shortcut.com/blog/more-reliable-webhooks-with-queues 
