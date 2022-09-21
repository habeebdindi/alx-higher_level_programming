#!/usr/bin/python3
for i in range(10):
    for i2 in range(10):
        if i2 != 0 and i2 > i:
            if i != 8:
                print("{0:d}{1:d}".format(i, i2), end=", ")
            elif i == 8:
                print("{0:d}{1:d}".format(i, i2))
