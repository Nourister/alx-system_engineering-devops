#!/usr/bin/python3
"""Contains recurse function"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent to avoid errors
    params = {'limit': 100, 'after': after}  # Limiting to 100 posts per request

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                hot_list.append(post['data']['title'])

            # Recursive call with the 'after' parameter to get the next page of results
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)
        else:
            if hot_list:
                return hot_list
            else:
                return None
    else:
        return None
