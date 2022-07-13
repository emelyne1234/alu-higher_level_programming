#!/usr/bin/python3
# printing reversely

def print_reversed_list_integer(my_list=[]):
for item in my_list:
    print_reversed_list_integer("{:d}".format(item))
