#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                   
    params = {}
    if after:
        params['after'] = after
                                        
    response = requests.get(url, headers=headers, params=params)
                                                
    if response.status_code != 200:
        return None
                                                                
    data = response.json()
                                                                    
    if 'data' not in data or 'children' not in data['data']:
        return None
                                                                                
    hot_list.extend([post['data']['title'] for post in data['data']['children']])

    after = data['data'].get('after')
                                                                                                                            
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
