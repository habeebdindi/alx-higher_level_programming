#!/usr/bin/python3
def no_c(my_string):
    _list = []
    _list[len(_list):] = my_string
    if 'C' in _list:
        _list.remove('C')
    elif 'c' in _list:
        _list.remove('c')
    _str = ""
    return _str.join(_list)
