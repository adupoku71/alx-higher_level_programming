#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """
    prints list items in reverse
    Args:
        my_list: list of integers

    Returns:
        None
    """

    for x in range(len(my_list) - 1, -1, -1):
        print('{:d}'.format(my_list[x]))
