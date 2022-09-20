#!/usr/bin/python3


def print_last_digit(number):
    last_digit = abs(number) % 10
    print('{:d}'.format(number), end='')
    return last_digit
