#!/usr/bin/python3
"""my_module.py

This module provides functions for interacting with the Reddit API. 
It includes functionality to retrieve the number of subscribers for a given subreddit."""
import requests

def number_of_subscribers(subreddit):
"""Function to return the number of subscribers of a subreddit
Keyword arguments: subreddit (a string return: return the number of subscribers of a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

