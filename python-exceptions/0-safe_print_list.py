#!usr/bin/bin/python3
# a function that prints elements of a list


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < x:
            print(my_list[count], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
