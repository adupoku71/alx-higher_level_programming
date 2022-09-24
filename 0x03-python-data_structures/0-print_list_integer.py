#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """print_list_integer

    Args:
        my_list: list of integers
    
    Returns:
        None

    """
    for x in my_list:
        print('{:d}'.format(x))


print_list_integer([1, 2, 3, 4, 5])
