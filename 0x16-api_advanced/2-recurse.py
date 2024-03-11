#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{subreddit}/hot/.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    hot_list.extend([post['data']['title'] for post in data['data']['children']])
    #If there are more posts, recurse with the 'after' parameter8
    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list