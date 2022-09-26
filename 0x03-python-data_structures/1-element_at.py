#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    else:
        for i in range(len(my_list)):
            if i == idx:
                for y in my_list:
                    return my_list[i]
