#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Base case: No more results
    if after == "":
        if not hot_list:
            return None  # If no results found
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Mozilla/5.0"}  # Add a User-Agent header to avoid 429 error (Too Many Requests)

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching data for subreddit '{subreddit}': {e}")
        return None

    if 'error' in data:
        print(f"Error: {data['message']}")
        return None

    children = data['data']['children']
    hot_list.extend([child['data']['title'] for child in children])

    after = data['data']['after']
    return recurse(subreddit, hot_list, after)