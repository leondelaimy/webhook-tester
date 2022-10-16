"""
Receiver of webhooks
"""
from hmac import HMAC, compare_digest
from hashlib import sha256
import os
import flask
import flask_lt
import redis
import rq
from processor.webhook import process_issue_comment

GITHUB_WEBHOOK_TOKEN = os.environ.get('GITHUB_WEBHOOK_TOKEN')

app = flask.Flask(__name__)
flask_lt.run_with_lt(app)


def verify_signature(req):
    """
    Verify GitHub webhook signature
    """
    received_sign = req.headers['X-Hub-Signature-256'].split(
        'sha256=')[-1].strip()
    secret = GITHUB_WEBHOOK_TOKEN.encode()
    expected_sign = HMAC(key=secret, msg=req.data,
                         digestmod=sha256).hexdigest()
    return compare_digest(received_sign, expected_sign)


@app.route('/', methods=['POST', 'GET'])
def receiver():
    """Listen for webhook event from GitHub"""
    if flask.request.method == 'POST':
        if verify_signature(flask.request):
            payload = flask.request.get_json()
            queue = rq.Queue(connection=redis.StrictRedis(host='redis'))
            queue.enqueue(process_issue_comment, payload)
            return "Webhook received", 200
        return 'Forbidden', 403
    return 'Not allowed', 405


if __name__ == '__main__':
    app.run()
