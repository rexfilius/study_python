"""
-> class bytes([source[, encoding[, errors]]])
Return a new 'bytes' object, which is an immutable sequence of integers in the
range 0 <= x < 256. bytes is an immutable version of bytearray – it has the same
non-mutating methods and the same indexing and slicing behavior.

Accordingly, constructor arguments are interpreted as for bytearray().
Bytes objects can also be created with literals.

-> callable(object)
Return True if the object argument appears callable, False if not. If this returns True,
it is still possible that a call fails, but if it is False, calling object will
never succeed. Note that classes are callable (calling a class returns a new instance);
instances are callable if their class has a __call__() method.

-> chr(i)
Return the string representing a character whose Unicode code point is the integer i.
e.g chr(97) returns the string 'a', while chr(8364) returns the string '€'.
This is the inverse of ord().

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16).
ValueError will be raised if i is outside that range.

-> @classmethod
Transform a method into a class method.A class method receives the class as implicit
first argument, just like an instance method receives the instance. To declare a
class method, use this idiom:

>>> class C:
...    @classmethod
...    def f(cls, arg1, arg2, ...): ...

A class method can be called either on the class (such as C.f()) or on an instance
(such as C().f()). The instance is ignored except for its class. If a class method
is called for a derived class, the derived class object is passed as the implied
first argument. Class methods are different than C++ or Java static methods.

-> compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
Compile the source into a code or AST (Abstract Syntax Tree) object. Code objects can
be executed by exec() or eval(). source can either be a normal string, a byte string,
or an AST object.

-> class complex([real[, imag]])
Return a complex number with the value [real + imag*1j] or convert a string or number
to a complex number.

-> delattr(object, name)
This is a relative of setattr(). The arguments are an object and a string. The string
must be the name of one of the object's attributes. The function deletes the named
attribute, provided the object allows it. e.g. delattr(x, 'foobar')
is equivalent to del x.foobar.

-> class dict(**kwarg)
-> class dict(mapping, **kwarg)
-> class dict(iterable, **kwarg)
Create a new dictionary. The dict object is the dictionary class.
"""
