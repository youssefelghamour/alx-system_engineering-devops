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

    users = requests.get(url_users).json()
    todos = requests.get(url_todos).json()

    dct1 = {}
    for user in users:
        lst = []
        for task in todos:
            if task['userId'] == user['id']:
                dct = {"username": user['username'],
                       "task": task['title'],
                       "completed": task['completed']}
                lst.append(dct)
        dct1[str(user['id'])] = lst

    json_filename = "todo_all_employees.json"

    with open(json_filename, 'w') as jsonfile:
        json.dump(dct1, jsonfile)
