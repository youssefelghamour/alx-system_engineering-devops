#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


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

    data = response.json()['data']
    posts = data['children']
    after = data['after']

    for post in posts:
        hot_list.append(post['data']['title'])

    if after:
        # get the next page
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
