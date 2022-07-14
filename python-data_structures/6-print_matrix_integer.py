#!/usr/bin/python3
# printing matrix


def print_matrix_integer(matrix=[[]]):
    for record in matrix:
        counter = 0
        for item in record:
            if counter == (len(record) - 1):
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
            counter += 1
        print()
