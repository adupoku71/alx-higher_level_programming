#!/usr/bin/python3


def multiple_returns(sentence):
    """
    returns a tuple with the length of a string and its first character
    """

    char_1 = sentence[0] if sentence else None

    return (len(sentence), char_1)
