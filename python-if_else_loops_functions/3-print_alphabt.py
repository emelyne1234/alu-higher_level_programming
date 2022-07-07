#!/usr/bin/python3
for i in range(97, 123):
    emlyn = chr(i)
    if emlyn not in "qe":
        print("{}".format(emlyn), end="")
