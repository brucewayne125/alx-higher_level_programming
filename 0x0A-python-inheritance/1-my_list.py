#!/usr/bin/python3
"""Defines an inherited class MyList"""


class MyList(list):
    """print_sorted: Dfines a subclass, MyList, of an inherited class, list"""

    def print_sorted(self):
        """prints a sorted list in ascending order"""
        print(sorted(self))
