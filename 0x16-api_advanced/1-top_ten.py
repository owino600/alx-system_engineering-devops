#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # If the subreddit is not valid, return None
    if response.status_code != 200:
        return None

    data = response.json()
    hot_list.extend([post['data']['title'] for post in data['data']['children']])

    # If there are more posts, recurse with the 'after' parameter
    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list