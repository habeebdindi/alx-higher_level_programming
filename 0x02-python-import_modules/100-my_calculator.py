#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    n = len(sys.argv)
    if n != 4:
        print("{}".format('Usage: ./100-my_calculator.py'
                          ' <a> <operator> <b>'))
        sys.exit(1)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, calc.add(a, b)))
        sys.exit(0)
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, calc.sub(a, b)))
        sys.exit(0)
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, calc.mul(a, b)))
        sys.exit(0)
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, calc.div(a, b)))
        sys.exit(0)
    else:
        print("{}".format('Unknown operator. Available operators:'
                          ' +, -, * and /'))
        sys.exit(1)
