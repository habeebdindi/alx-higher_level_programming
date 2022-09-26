#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = my_list[::-1]
    for i in x:
        print("{:d}".format(i))
