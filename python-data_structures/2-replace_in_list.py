#!/usr/bin/python3
# replacing in a list
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= range(len(my_list)):
        return my_list
