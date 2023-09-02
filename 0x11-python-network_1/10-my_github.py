#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/{}".format(username)
    auth = (username, password)
    retrieved = requests.get(url, auth=auth)
    json_data = retrieved.json()
    user_id = json_data.get("id")
    print(user_id)
