#!/usr/bin/python3
# retrieving an element from a list
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return 
    else:
        return my_list[idx]
