"""
-> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Print objects to the text stream file, separated by sep and followed by end.
sep, end, file and flush, if present, must be given as keyword arguments.

-> class property(fget=None, fset=None, fdel=None, doc=None)
Return a property attribute.

-> class range(stop)
-> class range(start, stop[, step])
Rather than being a function, range is actually an immutable sequence type.

-> repr(object)
Return a string containing a printable representation of an object.

-> reversed(seq)
Return a reverse iterator. seq must be an object which has a __reversed__() method
or supports the sequence protocol (the __len__() method and the __getitem__() method
with integer arguments starting at 0).

-> round(number[, ndigits])
Return number rounded to ndigits precision after the decimal point. If ndigits is
omitted or is None, it returns the nearest integer to its input.

-> class set([iterable])
Return a new set object, optionally with elements taken from iterable.
set is a built-in class.

-> setattr(object, name, value)
This is the counterpart of getattr(). The arguments are an object, a string and an
arbitrary value. The string may name an existing attribute or a new attribute.
The function assigns the value to the attribute, provided the object allows it.
e.g. setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

Note:: Since private name mangling happens at compilation time, one must manually
mangle a private attribute's (attributes with two leading underscores) name in order
to set it with setattr().

-> class slice(stop)
-> class slice(start, stop[, step])
Return a slice object representing the set of indices specified by
range(start, stop, step).
slice:: An object usually containing a portion of a sequence. A slice is created using
the subscript notation, [] with colons between numbers when several are given, such as
in variable_name[1:3:5]. The bracket (subscript) notation uses slice objects internally.

-> sorted(iterable, *, key=None, reverse=False)
Return a new sorted list from the items in iterable.

-> @staticmethod
Transform a method into a static method. A static method does not receive an implicit
first argument.
>>> class C:
...     @staticmethod
...     def f(arg1, arg2, ...): ...
The @staticmethod form is a function decorator. A static method can be called either on
the class (such as C.f()) or on an instance (such as C().f()).
Static methods in Python are similar to those found in Java or C++

Like all decorators, it is also possible to call staticmethod as a regular function
and do something with its result. This is needed in some cases where you need a
reference to a function from a class body and you want to avoid the automatic
transformation to instance method.
>>> class D:
...     builtin_open = staticmethod(open)
"""
