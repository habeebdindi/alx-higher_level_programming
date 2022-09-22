#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = (number * -1) % 10
        print("{}".format(n), end="")
    elif number >= 0:
        n = number % 10
        print("{}".format(n), end="")
    return n
