#!/usr/bin/python3
""" no modules used """


def inherits_from(obj, a_class):
    """ check if it inherits from that class """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
