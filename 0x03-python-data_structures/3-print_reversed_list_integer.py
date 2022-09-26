#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
   x = reversed(my_list)
   [print("{}".format(i)) for i in x]
