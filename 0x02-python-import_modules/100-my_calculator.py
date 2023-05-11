#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ops, mod = ['+', '-', '*', '/'], [add, sub, mul, div]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, op, b = sys.argv[1], sys.argv[2], sys.argv[3]
    for i in range(len(ops)):
        if op == ops[i]:
            print("{} {} {} = {:d}".format(a, op, b, mod[i](int(a), int(b))))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
