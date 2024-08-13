#!/usr/bin/python3
"""Function to query the Reddit API and return the number of 
subscribers for a given subreddit"""


import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "custom-agent"}
    
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        total_sub = results.get("subscribers")
        return total_sub
    else:
        return 0