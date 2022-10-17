"""
Process issue comment webhooks
"""

from processor.github import merge_pull_request

MERGE_COMMENT = '#merge'


def process_issue_comment(webhook_body):
    """
    Process an issue_comment event from GitHub.
    Called whenever GitHub sends a webhook as
    a result of a comment on a pull request thread.
    """
    action = webhook_body['action']
    user = webhook_body['sender']['login']
    issue_comment = webhook_body['comment']['body']
    pull_request_url = webhook_body['issue']['pull_request']['url']

    if action == 'created':
        print(f"Action: {action}")
        print(f"PR number: {webhook_body['issue']['number']}")
        print(f"Issue comment: {webhook_body['comment']['body']}")
        if issue_comment == MERGE_COMMENT:
            merge_pull_request(user, pull_request_url)
            print(f"Merge triggered by {user} for PR: {pull_request_url}")
