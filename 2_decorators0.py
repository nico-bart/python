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

n = 2
def ntimes(f):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            rv = f(*args, **kwargs)
            print('running {.__name__}'.format(f))
        return rv
    return wrapper

@ntimes
def add(x,y):
    return x + y


def sub(x,y):
    return x-y

print("add(10,20)", add(10,20))
print("add(20,30)", add(20,30))
print("sub(10,20)", sub(10,20))
print("sub(20,30)", sub(20,30))
