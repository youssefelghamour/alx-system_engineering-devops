#!/usr/bin/python3
""" script that, using this REST API: https://intranet.alxswe.com/
    for a given employee ID,
    returns information about his/her TODO list progress
"""
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

    print("Employee {} is done with tasks".format(users['name']), end="")

    nb_tasks = 0
    nb_tasks_completed = 0

    for task in todos:
        nb_tasks += 1
        if task['completed'] is True:
            nb_tasks_completed += 1

    print("({}/{}):".format(nb_tasks_completed, nb_tasks))

    for task in todos:
        if task['completed'] is True:
            print("\t {}".format(task['title']))
