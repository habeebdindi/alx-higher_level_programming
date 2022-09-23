#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    n = len(sys.argv)
    if n != 4:
        print("{}".format('Usage: ./100-my_calculator.py'
                          ' <a> <operator> <b>'))
        exit(1)
        for i in (1, n):
            fst = sys.argv[1]
            op = sys.argv[2]
            scd = sys.argv[3]
            a = int(fst)
            b = int(scd)
            if op != '+' or op != '-' or op != '*' or op != '/':
                print("{}".format('Unknown operator. Available operators:'
                                  ' +, -, * and /'))
                exit(1)
            elif op == '+':
                print("{} {} {} = {}".format(fst, op, scd, calc.add(a, b)))
                exit(0)
            elif op == '-':
                print("{} {} {} = {}".format(fst, op, scd, calc.sub(a, b)))
                exit(0)
            elif op == '*':
                print("{} {} {} = {}".format(fst, op, scd, calc.mul(a, b)))
                exit(0)
            elif op == '/':
                print("{} {} {} = {}".format(fst, op, scd, calc.div(a, b)))
                exit(0)
