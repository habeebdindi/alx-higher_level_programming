#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{:0>2d}".format(i), end=", ")
    elif i >= 10:
        if i != 99:
            print("{0:d}".format(i), end=", ")
        else:
            print("{:d}".format(i))
