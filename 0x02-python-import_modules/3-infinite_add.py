#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_arg = 0
    n = len(sys.argv)
    for i in range(1, n):
        sum_arg += int(sys.argv[i])
    print("", sum_arg)
