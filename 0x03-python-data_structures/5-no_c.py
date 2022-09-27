#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for st in my_string:
        if st not in ["C", "c"]:
            new = new + st
    return new
