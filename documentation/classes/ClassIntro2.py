# Class objects support two kinds of operations:
# => attribute references and instantiation.
# Attribute references use the standard syntax used for all attribute references in
# Python: "obj.name". Valid attribute names are all the names that were in the class'
# namespace when the class object was created.

# In the code below, "SimpleClass.i" & "SimpleClass.simple" are valid attribute
# references, returning an integer and a function object, respectively.
# Class attributes can also be assigned to, so you can change the value of
# "SimpleClass.i" by assignment.
# __doc__ is also a valid attribute, returning the docstring belonging to the
# class: "A simple class".
class SimpleClass:
    """A simple class"""
    i = 12345

    def simple(self):
        return 'hello world'


# Class instantiation uses function notation. Just pretend that the class object is a
# parameterless function that returns a new instance of the class
simple_class = SimpleClass()

"""
The instantiation operation ('calling' a class object) creates an empty object. 
Many classes like to create objects with instances customized to a specific initial 
state. Therefore a class may define a special method named __init__(), like this:

>>> def __init__(self):
...     self.data = []

When a class defines an __init__() method, class instantiation automatically invokes
__init__() for the newly-created class instance. Of course, the __init__() method may
have arguments for greater flexibility. In that case, arguments given to the class
instantiation operator are passed on to __init__().
"""


class ComplexNum:
    def __init__(self, realpart, imagpart):
        self.real = realpart
        self.imaginary = imagpart


complex_num = ComplexNum(3.0, 4.5)
print(complex_num.real)
print(complex_num.imaginary)
print()