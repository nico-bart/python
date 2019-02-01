# In Python a class statement is an executable code
# In C++ this is not the case!
#

# This defines a class 10 times in a row. Legit code
for _ in range(10):
  class Base: pass

# This defines a function 10 times in a row
class Base:
    for _ in range(10):
        def bar(self):
            pass


def testfunction():
    class Base:
        pass

#from dis import dis
#dis(testfunction)

old_bc = __build_class__
#def my_bc(*a, **kw):
def my_bc(function, name, base=None):
    if base = Base:
        print("Check if bar method is defined")
    if base is not None:
        return old_bc(function, name, base, **kw)
    else:
        return old_bc(function, name, **kw)

import builtins
builtins.__build_class__ = my_bc

class Base():
    pass
