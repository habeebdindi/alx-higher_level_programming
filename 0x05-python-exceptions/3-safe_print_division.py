#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a / b)
    except Exception as e:
        print(e)
    finally:
        if (b != 0):
            print("Inside result: {}".format(a / b))
