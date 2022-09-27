#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = my_list.copy()
    if idx < 0:
        return x
    elif idx > len(my_list) - 1:
        return x
    for i in range(len(my_list)):
        if i == idx:
            x[i] = element
            return x
