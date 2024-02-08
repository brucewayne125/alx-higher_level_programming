#!/usr/bin/python3

"""Defines a function that reads a text file (UTF8) and prints it to stdout."""
def read_file(filename=""):
    """prints the textfile in unicode to stdout."""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
