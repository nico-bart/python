
# We have this library.py file:
class Base:
  def fodo(self):
    return 'foo'

# We have this user code (bottom). How do prevent the following code to fail at runtime,
# if the library code has been messed with?
# To get the programm to fail before reaching the class-initialisation we can
# use the following code:

assert hasattr(Base, 'foo'), "You broke it, you fool!"
# This checks if the Base has the function "foo". If not, the error message is displayed

#from library import Base
class Derived(Base):
    def bar(self):
            return self.foo()
