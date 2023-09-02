#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    retrieved = response.read()

print("Body response:")
print("\t- type: {}".format(type(retrieved)))
print("\t- content: {}".format(retrieved))
print("\t- utf8 content: {}".format(retrieved.decode('utf-8')))
