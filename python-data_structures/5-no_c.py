#!/usr/bin/python3
# a function that removes all characters from a string


def no_c(my_string):
    temp = ' '

    for i in my_string:
        if (i.lower()) == 'c':
            continue
        temp += i
        return temp
