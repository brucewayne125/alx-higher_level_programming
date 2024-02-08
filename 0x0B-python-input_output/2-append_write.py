#!/usr/bin/python3

""" Defines a function that appends a string at the end of a text file (UTF8)."""



def append_write(filename="", text=""):
    """appends a string at the end of a text file
        filename: the file to which the string is appended to
        text: the text to be appended
        Return: the number of characters that are appended """
    with open(filename, 'a', encoding='utf-8') as myfile:
        myfile.write(text)
        return len(text)
