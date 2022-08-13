#!/usr/bin/python3
""" this module adds integers """


def add_integer(a, b=98):
    """ this function returns the addition of integers """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
