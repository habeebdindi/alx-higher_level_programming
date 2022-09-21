#!/usr/bin/python3
def uppercase(str):
    for w in str:
        x = ord(str)
        if x >= 97 and x < 123:
            x += 32
            print("{}".format(chr(str)), end="")
