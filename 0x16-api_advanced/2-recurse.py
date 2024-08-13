#!/usr/bin/python3
"""Recursively queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves the titles of all hot posts for a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(api_url, headers=headers,
                            params=params, allow_redirects=False)
    
    if not response.status_code != 200:
        return None
    
    data = response.json().get("data")
    if data is None:
        return None
    
    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title", "None"))
    
    after = data.get("after")
    if after is not None:

        return recurse(subreddit, hot_list, after)
    
    return hot_list
