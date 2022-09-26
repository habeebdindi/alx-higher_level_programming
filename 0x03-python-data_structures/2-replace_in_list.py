#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else: 
        for x in range(len(my_list)):
            if x == idx:
                for y in my_list:
                    if my_list[x] == element:
                        return my_list
                    elif my_list[x] != element:
                        my_list[x] = element
                        return my_list
