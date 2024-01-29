#!/usr/bin/python3
# a Python script that, using this REST API, for a given employee ID,
# returns information about his/her TODO list progress.
import requests
import sys
import re

# Define the base URL for the REST API
REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    # Check if command-line argument is provided
    if len(sys.argv) > 1:
        # Check if the argument is a positive integer using regular expression
        if re.fullmatch(r'\d+', sys.argv[1]):
            # Convert the argument to an integer (employee ID)
            id = int(sys.argv[1])

            # Fetch employee data and task data from the API
            req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()

            # Extract employee name
            emp_name = req.get('name')

            # Filter tasks for the given employee ID
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))

            # Filter completed tasks
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

            # Display employee's task progress
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )

            # Display titles of completed tasks if any
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))
