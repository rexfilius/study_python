"""
The syntax for a derived class definition looks like this:

>>> class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    <statement-N>

The name BaseClassName must be defined in a scope containing the derived class
definition. In place of a base class name, other arbitrary expressions are also allowed.
This can be useful, for example, when the base class is defined in another module:

>>> class DerivedClassName(modname.BaseClassName):

Execution of a derived class definition proceeds the same as for a base class. When the
class object is constructed, the base class is remembered. This is used for resolving
attribute references: if a requested attribute is not found in the class, the search
proceeds to look in the base class. This rule is applied recursively if the base
class itself is derived from some other class.

Derived classes may override methods of their base classes. Because methods have no
special privileges when calling other methods of the same object, a method of a base
class that calls another method defined in the same base class may end up calling
a method of a derived class that overrides it.

All methods in Python are effectively virtual. A virtual function is a member function
which is declared within a base class and is re-defined(Overridden) by a derived class.

An overriding method in a derived class may in fact want to extend rather than simply
replace the base class method of the same name. There is a simple way to call the base
class method directly: just call

>>> BaseClassName.methodname(self, arguments).

This is occasionally useful to clients as well. (Note that this only works if the
base class is accessible as BaseClassName in the global scope.)

Python has two built-in functions that work with inheritance:
[1] Use isinstance() to check an instance's type: isinstance(obj, int) will be True
only if obj.__class__ is int or some class derived from int.
[2] Use issubclass() to check class inheritance: issubclass(bool, int) is True since
bool is a subclass of int. However, issubclass(float, int) is False since
float is not a subclass of int.
"""
