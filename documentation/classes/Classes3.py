from documentation.classes.ClassIntro2 import SimpleClass

"""
The only operations understood by instance objects are attribute references. 
There are two kinds of valid attribute names: data attributes and methods.

data attributes correspond to "instance variables" in Smalltalk, and to "data members"
in C++. Data attributes need not be declared; like local variables, they spring into
existence when they are first assigned to.
"""
simple = SimpleClass()

simple.counter = 1
while simple.counter < 10:
    simple.counter = simple.counter * 2
print(simple.counter)
del simple.counter

"""
The other kind of instance attribute reference is a method. A method is a function
that "belongs to" an object. In Python, the term method is not unique to 
class instances: other object types can have methods as well. e.g. list objects 
have methods called append, insert, remove, sort, etc.

Valid method names of an instance object depend on its class. By definition, 
all attributes of a class that are function objects define corresponding methods 
of its instances.
"""
