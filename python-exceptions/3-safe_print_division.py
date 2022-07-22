#!/usr/bin/python3
# a function that divides 2 intgers and prints the result


def safe_print_division(a, b):
    try:
        result = (a/b)
    except (ValueError, RuntimeError, TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
