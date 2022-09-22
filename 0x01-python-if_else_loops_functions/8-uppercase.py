#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) >= 97 and ord(w) < 123:
            print("{}".format(chr(ord(w) - 32)), end="")
        elif ord(w) >= 0 and ord(w) < 97:
            print("{}".format(chr(ord(w))))
