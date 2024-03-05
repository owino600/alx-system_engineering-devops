#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    try:
        # Set a custom User-Agent to avoid Too Many Requests errors
        headers = {'User-Agent': 'MyRedditBot'}
        
        # Make an API request to get hot posts
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Extract and print post titles
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    except (KeyError, requests.RequestException):
        # Invalid subreddit or other error occurred
        print(None)

# Example usage:
subreddit_name = 'learnprogramming'
top_ten(subreddit_name)