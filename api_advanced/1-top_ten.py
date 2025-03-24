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

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status() 

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"]["title"])
        print("OK") .

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(None)
        else:
            print(None)

    except (requests.exceptions.RequestException, KeyError, ValueError):
        print(None)
