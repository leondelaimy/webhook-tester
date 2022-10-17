"""
GitHub API calls
"""
import os
import json
import requests

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')
headers = {
    'Authorization': f"Bearer {GITHUB_ACCESS_TOKEN}",
    'Accept': 'application/vnd.github+json'
}


def get_pull_request(user, url):
    """
    Call GitHub API to get pull request
    """
    try:
        response = requests.get(f"{url}", headers=headers, timeout=30)
        pull = response.json()
        response.raise_for_status()
        head_sha = pull['head']['sha']
        base_ref = pull['base']['ref']
        data = {
            'pull': {
                'head_sha': head_sha,
                'base_ref': base_ref
            },
            'requester': user
        }
        return data
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


def merge_pull_request(user, url):
    """
    Call GitHub API to merge pull request into main
    """
    try:
        pull_request = get_pull_request(user, url)
        data = {
            'commit_title': 'Merge PR',
            'commit_message': f"Merge triggered by {user} for PR: {url}",
            'sha': pull_request['pull']['head_sha']
        }
        response = requests.put(
            f"{url}/merge", headers=headers, data=json.dumps(data), timeout=30)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
