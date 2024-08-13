#!/usr/bin/python3
"""Function to query the Reddit API and return the number of 
subscribers for a given subreddit"""

import requests
import json


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    
    api_url = "https://www.reddit.com/r/{}/about.json"
    HEADER = {"User-Agent": "custome-agent"}
    
    try:
        url = api_url.format(subreddit)
        
        response = requests.get(url, headers=HEADER, allow_redirects=False)
        
        if response.status_code == 200:
            data = json.loads(response.text)
            subscribers = data["data"]["subscribers"]
            return subscribers
             
        else:
            return 0
       
    except Exception:
        """If no valid subreddit return 0"""
        return 0