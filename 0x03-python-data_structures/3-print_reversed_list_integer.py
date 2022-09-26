#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
   x = []
   x = reversed(my_list)
   for i in x:
       if isinstance(i, float):
           print("{:f}".format(i))
       elif isinstance(i, int):
           print("{:d}".format(i))
