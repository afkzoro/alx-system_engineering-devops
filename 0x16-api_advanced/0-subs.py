#!/usr/bin/python3
""" Queries Reddit API and returns number of subs on a subreddit or 0"""
import requests

def number_of_subscribers(subreddit):
    """ Function to get number of subs on a subreddit"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"""
    }
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
