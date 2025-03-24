#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top 10 hot posts
    for a given subreddit.

    If the subreddit is invalid, it prints None.
    If the request is successful, it prints the titles and "OK".
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
        print("OK") #Added this line to print "OK" on success.

    except (KeyError, ValueError, requests.exceptions.RequestException):
        print(None)
