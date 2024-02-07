#!/usr/bin/python3
def lookup(obj):
"""call the dir() function with the obj argument and return the resulting list."""
    return dir(obj)

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
