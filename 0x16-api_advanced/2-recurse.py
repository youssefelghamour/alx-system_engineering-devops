#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def add_title(hot_list, posts):
    """ appends post titles to the hot_list """
    if len(posts) == 0:
        return

    hot_list.append(posts[0]['data']['title'])

    posts.pop(0)

    add_title(hot_list, posts)


def recurse(subreddit, hot_list=[], after=None):
    """ queries the Reddit API and prints the titles of the first 10 hot
        posts listed for a given subreddit.
    """
    CLIENT_ID = 'zL8evAsF03DzVk_TArVH3g'
    SECRET_KEY = 'FT7BTQs-WLEtZEOlH_2mE2QEQ8CV2g'

    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

    data = {
        'grant_type': 'password',
        'username': 'Responsible-Big4336',
        'password': 'password123'
    }

    headers = {'User-Agent': 'MyAPI1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    TOKEN = res.json()['access_token']

    headers['Authorization'] = "bearer {}".format(TOKEN)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    response = requests.get(url, auth=auth, data=data, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    add_title(hot_list, posts)

    after = data['data']['after']

    if not after:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)
