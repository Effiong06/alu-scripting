#!/usr/bin/python3
import requests
import re

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}
                        
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
                                                                                                
    posts = data['data']['children']
    after = data['data'].get('after')
                                                                                                                
    for post in posts:                                                                           
        title = post['data']['title'].lower()                                                                                    
        
        for word in word_list:
            word = word.lower()
            matches = re.findall(r'\b' + re.escape(word) + r'\b', title)
            counts[word] += len(matches)                                                                                                                    
 
    if after:
        return count_words(subreddit, word_list, after, counts)
                        
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                                
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
