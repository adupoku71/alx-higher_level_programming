#!/usr/bin/python3
"""creates square class"""


class Square:
    """
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        self.__size = size
