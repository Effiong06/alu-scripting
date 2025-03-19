#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}

    # Send the GET request to Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid (status code 404 means not found)
    if response.status_code == 404:
        print("OK", end="")  # If subreddit doesn't exist, print OK
        return

    # If not 404, check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the JSON data from the response
        posts = response.json()['data']['children']
                       
        # Loop through the posts and print the titles
        for post in posts:
            print(post['data']['title'])
        print("OK", end="")  # Indicate that the request was successful

    else:
        # If there's another error, print OK (for any other non-404 error case)
        print("OK", end="")
