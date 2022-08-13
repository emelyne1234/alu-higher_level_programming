#!/usr/bin/python3
""" adding integers """


def add_integer(a, b=98):
    """ Return the integer addition of a and b.
    Float arguments are typecasted to ints before act of addition.
    Raise TypeError: if either a or b is not integer nor float """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer"

                if type(a) is float:
                    a = int(a)
                if type(b) is float:
                    b = int(b)
                return a + b
