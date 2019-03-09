# decorators.py

def add(x, y):
    return x + y

add(1, 2)

# Function call without () returns physical location of function
print("Physical location of function:")
print(add)

# add.__name__ returns name of function
print("Name of function:")
print(add.__name__)

# returns module to which this function belongs
print("Module where to find the function:")
print(add.__module__)

# returns defaults
print("Default values of the function:")
print(add.__defaults__)

# returns the bytecode of the function
print("The bytecode of the function:")
print(add.__code__.co_code)

# how many local variables does the function have?
print("The amount of local variables:")
print(add.__code__.co_nlocals)

# returns variable names
print("The names of the variables:")
print(add.__code__.co_varnames)

# returns source code of function
print("Source code of the function:")
from inspect import getsource
print(getsource(add))

# example for a decorator code
from time import time
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("Elapsed:", after - before)
        return rv
    return f

# The following syntaxes are identical
# the @timer syntax adds the decorator "timer" to add
@timer
def add(x,y):
    return x + y

# the sub=timer(sub) adds the decorator "timer" to sub
def sub(x,y):
    return x-y
sub = timer(sub)

print("add(10,20)", add(10,20))
print("add(20,30)", add(20,30))
print("sub(10,20)", sub(10,20))
print("sub(20,30)", sub(20,30))
