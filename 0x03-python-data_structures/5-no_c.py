#!/usr/bin/python3
def no_c(my_string):
    _list = []
    for ch in my_string:
        if ch != 'C' and ch != 'c':
            _list.append(ch)
    string = "".join(_list)
    return string
