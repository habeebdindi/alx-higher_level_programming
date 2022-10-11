#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
        except IndexError:
            c = c - 1
            break
    print("")
    try:
        return c + 1
    except UnboundLocalError:
        return 0
