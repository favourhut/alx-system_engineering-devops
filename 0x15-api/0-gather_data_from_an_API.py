#!/usr/bin/python3
"""Python script that, using this REST API, for a 
given employee ID, returns information 
about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    
    api_url = "https://jsonplaceholder.typicode.com"
    request = requests.get(api_url + "user/{}".format(argv[1])).json
    get_todo = requests.get(api_url + "todos/{}".format(argv[1])).json
    
    print(get_todo)