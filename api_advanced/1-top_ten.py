#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers, params={'limit': 10})
                    
    if response.status_code != 200:
        print(None)
        return
                                            
    data = response.json()
    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            print(post['data']['title'])
        else:
            print(None)
