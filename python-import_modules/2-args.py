#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    values = sys.argv
    i = len(values) - 1

    if i == 0:
    print("{} arguments".format(i))
elif i == 1:
    print("{} arguments".format(i))
else:
    print("{} arguments".format(i))

    if i >= 1:
        i = 0
        for arg in values:
            if i != 0:
                print("{}: {}".format(i, arg))
                i +=  1