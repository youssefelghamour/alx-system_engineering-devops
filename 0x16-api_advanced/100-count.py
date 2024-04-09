#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """ recursively queries the Reddit API, parses titles,
        and counts keyword occurrences
    """

    if counts is None:
        counts = {}

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
        title = post['data']['title'].lower()
        unique_words = set(title.split())
        for word in word_list:
            word = word.lower()

            if word in unique_words:
                # Get the current count for the word or default to 0
                count = counts.get(word, 0)
                # Increment the count by 1 and update the dictionary
                counts[word] = count + 1

    if after:
        return count_words(subreddit, word_list, after, counts)
    else:
        # Converts the counts dict into a list of tuples [(word, count), ...]
        # Sorts the list in descending order by turning the counts (x[1] in
        # the tuple) to negative numbers during sorting,
        # which ensures that bigger numbers come first
        # When words have the same count, they are sorted alphabetically (x[0])
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
