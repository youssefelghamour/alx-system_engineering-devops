#!/usr/bin/python3
""" script that, using this REST API: https://intranet.alxswe.com/
    for a given employee ID,
    returns data about his/her TODO list progress
    and exports this data in the CSV format
"""
import csv
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

    csv_filename = "{}.csv".format(user_id)

    with open(csv_filename, 'w') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([user_id,
                             user_name,
                             task["completed"],
                             task["title"]
                             ])
