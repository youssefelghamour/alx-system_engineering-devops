#!/usr/bin/python3
""" script that, using this REST API: https://intranet.alxswe.com/
    for a given employee ID,
    returns data about his/her TODO list progress
    and exports this data in the json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users/"
    url_todos = "https://jsonplaceholder.typicode.com/todos/"

    user_id = sys.argv[1]

    url_users = url_users + user_id
    url_todos = url_todos + "/?userId=" + user_id

    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    user_name = users['username']

    lst = []
    for task in todos:
        dct = {"task": task['title'],
               "completed": task['completed'],
               "username": user_name}

        lst.append(dct)

    dct1 = {str(user_id): lst}
    json_filename = "{}.json".format(user_id)

    with open(json_filename, 'w') as jsonfile:
        json.dump(dct1, jsonfile)
