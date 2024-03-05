#!/usr/bin/python3
"""my python"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: Total number of subscribers, or 0 if the subreddit is invalid.
    """
    try:
        # Set a custom User-Agent to avoid Too Many Requests errors
        headers = {'User-Agent': 'MyRedditBot'}
        
        # Make an API request to get subreddit information
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Extract the subscriber count
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, requests.RequestException):
        # Invalid subreddit or other error occurred
        return 0

# Example usage:
subreddit_name = 'learnprogramming'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers in r/{subreddit_name}: {subscribers_count}")