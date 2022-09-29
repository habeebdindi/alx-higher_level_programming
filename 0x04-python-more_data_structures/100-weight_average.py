#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = [num[0] * num[1] for num in my_list]
    n = sum(x)
    res = n / sum([num[1] for num in my_list])
    return res
