#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 2):
        print("{:d} argument:".format(1))
        print("{:d}: {}".format(1, sys.argv[1]))
    elif (len(sys.argv) == 1):
        print("{:d} arguments.".format(0))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for args in range(1, len(sys.argv)):
            print("{:d}: {}".format(args, sys.argv[args]))
