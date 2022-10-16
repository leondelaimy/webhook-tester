"""
Receiver of webhooks
"""
import flask
import flask_lt
import redis
import rq
from processor.webhook import process_issue_comment

app = flask.Flask(__name__)
flask_lt.run_with_lt(app)


@app.route('/', methods=['POST'])
def receiver():
    """Listen for webhook event from GitHub"""
    payload = flask.request.get_json()
    queue = rq.Queue(connection=redis.StrictRedis(host='redis'))
    queue.enqueue(process_issue_comment, payload)
    return ("Webhook received", 200, None)


if __name__ == '__main__':
    app.run()
