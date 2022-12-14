#!/usr/bin/python3
from sys import argv as args
from calculator_1 import add, sub, mul, div


if __name__ == '__main__':
    # print(args)
    op_dict = {
            '+': add,
            '-': sub,
            '/': div,
            '*': mul
    }

    if len(args) - 1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        if args[2] not in ('+', '-', '/', '*'):
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            op = args[2]
            x = op_dict[op](a, b)

            print('{:d} {} {:d} = {:d}'.format(a, op, b, x))
