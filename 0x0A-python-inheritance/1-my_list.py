#!/usr/bin/python3
class MyList(list):
#print_sorted: Dfines a subclass, MyList, of an inherited class, list     
    def print_sorted(self):
    #prints a sorted list
        sorted_list = sorted(self)
        print(sorted_list)