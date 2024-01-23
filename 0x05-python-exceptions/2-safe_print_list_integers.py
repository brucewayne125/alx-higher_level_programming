#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    i = 0
    while ret < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list, end"")
                ret = ret + 1
        except(ValueError, TypeError,IndexError):
        break

        i = i + 1
    print("")
    return ret

