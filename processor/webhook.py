"""
Process issue comment webhooks
"""
MERGE_SERVICE_URL = 'merger.example.com'
ORGANISATION = 'Example'
MERGE_COMMENT = '#merge'


def process_issue_comment(webhook_body):
    """
    Process an issue_comment event from GitHub.
    Called whenever GitHub sends a webhook as a result of a comment on a pull request thread.
    """
    action = webhook_body['action']
    user = webhook_body['sender']['login']
    issue_comment = webhook_body['comment']['body']

    print(f"Action: {action}")
    print(f"PR number: {webhook_body['issue']['number']}")
    print(f"Issue comment: {webhook_body['comment']['body']}")

    if action == 'created':
        if issue_comment == MERGE_COMMENT:
            print(f'Merge triggered by {user}')
