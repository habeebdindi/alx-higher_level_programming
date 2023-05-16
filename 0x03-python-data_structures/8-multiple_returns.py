#!/usr/bin/python3
def multiple_returns(sentence):
    first, length = "", len(sentence)
    if length == 0:
        first += "None"
    else:
        first += sentence[0]
    ret = (length, first)
    return ret
