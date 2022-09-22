#!/usr/bin/python3
def uppercase(str):
    for w in str:
        x = ord(w)
        if x >= 97 and x < 123:
            x += 32
            z = chr(x)
            print("{}".format(z), end="")
