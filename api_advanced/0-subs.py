#!/usr/bin/python3
"""
This module defines a function 'number_of_subscribers' that queries the Reddit API
to return the number of subscribers for a given subreddit. If the subreddit is invalid,
it returns 0.

The function makes a request to the Reddit API and checks the response for the 'subscribers'
field to extract the subscriber count.
"""
import requests

def number_of_subscribers(subreddit):
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return 0

       data = response.json()

       if 'data' in data and 'subscribers' in data['data']:
           return data['data']['subscribers']
       else:
           return 0
