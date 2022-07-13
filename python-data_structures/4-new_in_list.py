#!/usr/bin/python3
# replacing an element in a list at a specific position


def new_in_list(my_list, idx, elements):
    if idx < 0 or idx >= len(my_list):
        copy_it = my_list[:]
        return copy_it
    else:
        copy_em = my_list[:]
        copy_em[idx] = element
        return copy_em
