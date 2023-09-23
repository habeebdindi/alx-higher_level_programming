#!/usr/bin/python3
"""
Python script that fetches a url and prints a specific header value
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    retrieved = requests.get(url)
    retrieved = retrieved.headers
    print(retrieved.get("X-Request-Id"))
