#!/usr/bin/python3
""" function that queries the Reddit API """
import requests
after = None


def count_words(subreddit, word_list):
    """Count the titles found with wordlist in subreddit"""
    my_list = recurse(subreddit)
    my_dict = {}

    if my_list:
        for word in word_list:
            word = word.lower()
            my_dict[word] = 0

        for title in my_list:
            title_split = title.split(" ")

            for iter in title_split:
                for iter_split in word_list:
                    if iter.lower() == iter_split.lower():
                        my_dict[iter_split.lower()] = my_dict.get(iter_split.lower(), 0) + 1

        for key, val in sorted(my_dict.items(),  key=lambda x: x[1],
                               reverse=True):
            if val != 0:
                print("{}: {}".format(key, val))


def recurse(subreddit, hot_list=[]):
    """ recursively queries the Reddit API, parses titles,
        and counts keyword occurrences
    """
    global after
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

    if response.status_code == 200:
        prox = response.json().get('data').get('after')

        if prox is not None:
            after = prox
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')

        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title').lower())
        return hot_list
    else:
        return (None)
