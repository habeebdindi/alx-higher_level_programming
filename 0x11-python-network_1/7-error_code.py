#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    retrieved = requests.get(url)
    if retrieved.status_code >= 400:
        print("Error code: {}".format(retrieved.status_code))
    else:
        print(retrieved.text)
