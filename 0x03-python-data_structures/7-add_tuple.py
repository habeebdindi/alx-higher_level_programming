#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = (0, 0)
    tup1 = tuple_a + new
    tup2 = tuple_b + new
    new = tup1[0] + tup2[0], tup1[1] + tup2[1]
    return new
