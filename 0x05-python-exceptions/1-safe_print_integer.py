#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return 0
    except(ValueError, TypeError):
        return 1
