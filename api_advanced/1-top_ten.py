#!/usr/bin/python3
"""
A module that prints the titles of the top
10 hot posts from a subreddit.
"""
import requests

def top_ten(subreddit):
    """ 
    prints the titles of the first 10 hot posts listed in a subreddit 
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("OK")
        return

    try:
        posts = response.json()['data']['children']
    except KeyError:
        print("OK")
        return

    for post in posts:
        print(post['data']['title'])
                              
    print("OK")
