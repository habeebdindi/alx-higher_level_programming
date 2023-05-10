#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            new_str = new_str + chr(ord(letter) - 32)
        else:
            new_str = new_str + letter
    print("{}".format(new_str))
