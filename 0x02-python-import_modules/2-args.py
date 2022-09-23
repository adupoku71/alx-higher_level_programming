#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    sys_args = len(args)

    if sys_args == 1:
        string = 'arguments.'
    elif sys_args == 2:
        string = 'argument:'
    else:
        string = 'arguments:'
    print('{:d} {}'.format(sys_args - 1, string))
    for i in range(1, sys_args):
        print('{:d}: {}'.format(i, args[i]))
