#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            returned = response.read().decode('utf-8')
        print(returned)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
