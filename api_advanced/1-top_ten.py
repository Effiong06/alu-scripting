#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return
                                            
    data = response.json()

    if 'data' not in data or 'children' not in data['data']:
        print(None)
        return
    
    posts = data['data']['children']
    for i in range(min(10, len(posts))):
        print(posts[i]['data']['title'])
