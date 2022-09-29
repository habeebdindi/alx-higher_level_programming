#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for xe in sorted(a_dictionary):
        print("{}: {}".format(xe, a_dictionary[xe]))
