#!/usr/bin/python3
# a Python script that, using this REST API, for a given employee ID,
# returns information about his/her TODO list progress.
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    employee_url = f"{base_url}/{employee_id}"

    # Get employee details
    response_employee = requests.get(employee_url)
    if response_employee.status_code != 200:
        print(f"Error fetching employee details. Status code: {response_employee.status_code}")
        return

    employee_data = response_employee.json()
    employee_name = employee_data.get('name')

    # Get employee's TODO list
    todo_url = f"{employee_url}/todos"
    response_todo = requests.get(todo_url)
    if response_todo.status_code != 200:
        print(f"Error fetching TODO list. Status code: {response_todo.status_code}")
        return

    todo_list = response_todo.json()

    # Calculate progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    print(f"{employee_name}: {completed_tasks}/{total_tasks}")

    # Display titles of completed tasks
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
