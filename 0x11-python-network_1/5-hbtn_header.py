#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    retrieved = requests.get(url)
    retrieved = retrieved.headers
    print(retrieved.get("X-Request-Id"))
