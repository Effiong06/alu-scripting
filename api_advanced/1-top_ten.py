#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """
    A function that fetches and prints the titles of the top ten hot posts
    from a subreddit, or prints 'OK' if successful, or 'None' if failed.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"]["title"])
        print("OK") # prints OK if it succeeds.

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(None)
        else:
            print(None)

    except (requests.exceptions.RequestException, KeyError, ValueError):
        print(None)
