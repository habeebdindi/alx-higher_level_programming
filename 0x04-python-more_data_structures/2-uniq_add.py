#!/usr/bin/python3
def uniq_add(my_list=[]):
    l = []
    for num in my_list:
        if num not in l:
            l.append(num)
    return sum(l)
