#!/usr/bin/python3
""" Queries Reddit API and returns number of subs on a subreddit or 0"""
import requests


def number_of_subscribers(subreddit):
    """ Function to get number of subs on a subreddit"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(link, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
