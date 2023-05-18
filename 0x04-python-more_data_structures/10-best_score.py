#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxv = float('-inf')
    maxk = None
    for k, v in a_dictionary.items():
        if v > maxv:
            maxk = k
            maxv = v
    return maxk
