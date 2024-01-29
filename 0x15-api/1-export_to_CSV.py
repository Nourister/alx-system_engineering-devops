#!/usr/bin/python3
""" Python script to export data in the CSV format"""

import sys
import requests
import csv

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    resp = requests.get(url_user)
    user_name = resp.json().get('username')
    task = url_user + '/todos'
    resp = requests.get(task)
    tasks = resp.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            title_task = task.get('title')
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
