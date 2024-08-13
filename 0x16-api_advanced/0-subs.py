#!/usr/bin/python3
"""Function to query the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.""" 
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0x16. API advanced:projects"}
    
    response = requests.get(api_url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json().get("data")
        return results.get("subscribers")