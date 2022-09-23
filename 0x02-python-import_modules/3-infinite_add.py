#!/usr/bin/python3
import sys

if __name__ == '__main__':
    summ = 0
    args = sys.argv
    for i in range(1, len(args)):
        summ += int(args[i])

    print(summ)
