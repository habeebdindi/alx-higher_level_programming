#!/usr/bin/python3
def safe_print_integer(value):
    try:
        converted = int(value)
        print("{:d}".format(converted))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
