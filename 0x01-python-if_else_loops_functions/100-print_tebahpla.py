#!/usr/bin/python3
def reverse_alphabet():
    for i in range(122, 96 -1, -2):
        print("{:c}".format(i) + "{:c}".format(i - 33), end="")
