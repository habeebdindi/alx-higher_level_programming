#!/usr/bin/python3
def uniq_add(my_list=[]):
    li = []
    for num in my_list:
        if num not in li:
            li.append(num)
    return sum(li)
