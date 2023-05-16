#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a, l_b, sum = list(tuple_a), list(tuple_b), []
    for i in range(2):
        l_a.append(0)
        l_b.append(0)
    sum = [l_a[0] + l_b[0], l_a[1] + l_b[1]]
    return tuple(sum)
