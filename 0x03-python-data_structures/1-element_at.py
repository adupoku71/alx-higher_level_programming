#!/usr/bin/python3


def element_at(my_list, idx):
    """

    Args:
        my_list: list of elements
        idx: positive list index

    Returns:
        element at index idx

    """

    if idx > len(my_list) - 1 or idx < 0:
        return None

    return my_list[idx]
