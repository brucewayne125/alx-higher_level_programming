#!/usr/bin/python3
#python3 -c 'print(__import__("my_module").__doc__)'
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass
#python3 -c 'print(__import__("my_module").MyClass.__doc__)'
class MyClass2(object):
#python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
