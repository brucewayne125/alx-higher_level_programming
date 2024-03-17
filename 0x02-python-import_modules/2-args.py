#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv) - 1
    if num_arg < 1:
        print("{} arguments.".format(num_arg))
    elif num_arg == 1:
        print("{} arguments:".format(num_arg))
    else:
        print("{} arguments:".format(num_arg))
    for i in range(num_arg):
        print("{}: {:s}".format(i + 1, argv[i + 1]))   
