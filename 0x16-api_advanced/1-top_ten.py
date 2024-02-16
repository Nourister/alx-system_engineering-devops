#!/usr/bin/python3
"""  a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Custom User-Agent to avoid errors
    params = {'limit': 10}  # Limiting to 10 posts

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            print(f"Top 10 hot posts in r/{subreddit}:")
            for post in posts:
                print(post['data']['title'])
        else:
            print(f"No posts found in r/{subreddit}")
    else:
        print("None")  # Invalid subreddit or request failed
