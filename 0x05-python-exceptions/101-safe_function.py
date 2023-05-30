#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        msg = "Exception: {}\n".format(e)
        sys.stderr.write(msg)
        return None
