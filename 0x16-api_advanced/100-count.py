#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

from collections import Counter
from re import findall
import requests

def count_words(subreddit, word_list, after="", word_count=Counter()):
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(base_url, headers=headers, params=params)

    if not response.status_code == 200:
        return

    data = response.json().get('data', {})
    after = data.get('after', "")
    posts = data.get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', "")
        words = findall(r'\b\w+\b', title.lower())
        word_count += Counter(word for word in words if word in word_list)

    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        for word, count in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(word, count))