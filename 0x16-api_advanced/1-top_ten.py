#!/usr/bin/python3
"""prints the titles of the first 10 hot posts in a subreddit."""

import requests


def top_ten(subreddit):
    """If not a valid subreddit, print None"""
    api_url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 "}
    params = {"limit": 10}
    
    response = requests.get(api_url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(post.get("data").get("title")) for post in results.get("children")]
