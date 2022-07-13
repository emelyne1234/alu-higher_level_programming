#!/usr/bin/python3
# replacing an element in a list at a specific position

def new_in_list(my_list, idx, elements):
    if idx < 0 or idx >= len(my_list):
        return copy(my_list)
    else:
        my_list[idx] = element
        return my_list
