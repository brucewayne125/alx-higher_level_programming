#!/usr/bin/python3
#python3 -c 'print(__import__("my_module").__doc__)'
#python3 -c 'print(__import__("my_module").my_function.__doc__)'
#python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
def lookup(obj):
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
