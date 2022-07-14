#!/usr/bin/python3
# printing reversely


def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        count = len(my_list) - 1
        if count >= 0:
            for item in my_list:
                print("{:d}".format(item))
                count -= 1
