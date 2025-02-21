#!/usr/bin/python3
"""
This module defines a function 'count_words' that queries the Reddit API and parses
the titles of hot posts, counting the occurrences of specified keywords (case-insensitive).
The results are printed in descending order by count, and alphabetically for tied counts.

The function handles pagination and recursively collects post titles. It then counts
keyword occurrences and prints the sorted results. If the subreddit is invalid or no results
are found, nothing is printed.
"""
import requests
import re

def count_words(subreddit, word_list, word_count={}, after=None):
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
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            # Create a regex pattern to match the keyword as a whole word (case-insensitive)
            word_pattern = r'\b' + re.escape(word.lower()) + r'\b'
            word_count[word] = word_count.get(word, 0) + len(re.findall(word_pattern, title))

    after = data['data'].get('after')
    if after:
        return count_words(subreddit, word_list, word_count, after)
                                                                                                                            # Sorting the results
    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
