#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} {}".format(len(sys.argv) - 1, "arguments."))
    elif len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            print("{} {}:".format(len(sys.argv) - 1, "argument"))
            print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
        elif len(sys.argv) > 2:
            print("{} {}:".format(len(sys.argv) - 1, "arguments"))
            for w in range(2, len(sys.argv) + 1):
                print("{}: {}".format(w - 1, sys.argv[w - 1]))
