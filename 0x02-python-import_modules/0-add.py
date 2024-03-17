#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_o.py import add
    print ("{} + {} = {}".format(a, b, add(a, b)))
