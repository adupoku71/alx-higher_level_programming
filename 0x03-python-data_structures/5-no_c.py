#!/usr/bin/python3


def no_c(my_string):
    new_string = ''

    for char in my_string:
        if ord(char) not in [99, 67]:
            new_string += char

    return new_string
