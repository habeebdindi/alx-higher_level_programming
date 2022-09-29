#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = my_list.copy()
    new = []
    for idx, i in enumerate(cpy):
        if i == search:
            cpy[idx] = replace
    return cpy
