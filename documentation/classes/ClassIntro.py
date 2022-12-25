"""
Classes provide a means of bundling data and functionality together. Creating a new
class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.

Python classes provide all the standard features of Object Oriented Programming: the
class inheritance mechanism allows multiple base classes, a derived class can override
any methods of its base class or classes, and a method can call the method of a base
class with the same name.

Objects can contain arbitrary amounts and kinds of data. As is true for modules,
classes partake of the dynamic nature of Python: they are created at runtime,
and can be modified further after creation.
"""

"""
Class Definition Syntax::

Class definitions, like function definitions must be executed before they have any 
effect. (You could conceivably place a class definition in a branch of an if statement,
or inside a function.)

In practice, the statements inside a class definition will usually be function 
definitions, but other statements are allowed, and sometimes useful. The function 
definitions inside a class normally have a peculiar form of argument list, 
dictated by the calling conventions for methods.

When a class definition is entered, a new namespace is created, and used as the local 
scope — thus, all assignments to local variables go into this new namespace. 
In particular, function definitions bind the name of the new function here.
"""