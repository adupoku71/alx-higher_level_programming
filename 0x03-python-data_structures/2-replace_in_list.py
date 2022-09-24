#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """

    Args:
        my_list: list of items
        idx: positive list index
        element: item to insert into list

    Returns:
        my_list if idx is less than 0 or out of range

    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element
