#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = reversed(my_list)
    for i in x:
        print("{:d}".format(i))
