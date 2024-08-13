#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


<<<<<<< HEAD
def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves the titles hot posts"""
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

=======
def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
>>>>>>> 13d9e89e8e9e526f62e1eef6965b674cce4ca246
    return hot_list
