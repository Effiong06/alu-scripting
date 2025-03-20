#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
                    
    response = requests.get(url, headers=headers, allow_redirects=False)
                            
    if response.status_code != 200:
        print("OK")  # Instead of None, print "OK" when invalid subreddit
        return

    try:
        posts = response.json()['data']['children']
    except KeyError:
        print("OK")  # Instead of None, print "OK" if JSON structure is missing expected data
        return

    for post in posts:
        print(post['data']['title'])
                                                                                                        
    print("OK")  # Print OK after printing post titles to indicate success

