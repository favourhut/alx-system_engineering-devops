#!/usr/bin/python3
"""Python script that, using this REST API, for a 
given employee ID, returns information 
about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":
    
    api_url = "https://jsonplaceholder.typicode.com"
    req = requests.get(api_url + "user/{}".format(argv[1])).json
    get_todo = requests.get(api_url + "todos", params={"userId" (argv[1])}).json
    
    result = [i.get("title") for i in get_todo if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        req.get("name"), len("result"), len(get_todo)))
            
    for i in result:
        print("\t {}".format(i))