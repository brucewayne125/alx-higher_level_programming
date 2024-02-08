#!/usr/bin/python3

""" Defines a function that writes a string to a text file (UTF8) and returns the number of characters written."""



def write_file(filename="", text=""):
    """ writes a string in unicode and return: the length of the char."""
    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.write(text)
        return len(text)
