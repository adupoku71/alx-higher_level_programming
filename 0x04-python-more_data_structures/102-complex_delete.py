#!/usr/bin/python3


def complex_delete(a_dictionary, value):

    if not a_dictionary:
        return None

    for key, data in a_dictionary.copy().items():
        if data == value:
            del a_dictionary[key]

    return a_dictionary.copy()
