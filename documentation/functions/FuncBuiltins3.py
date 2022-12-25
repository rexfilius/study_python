"""
-> dir([object])
Without arguments, return the list of names in the current local scope. With an argument,
attempt to return a list of valid attributes for that object.

-> divmod(a, b)
Take two (non complex) numbers as arguments and return a pair of numbers consisting of
their quotient and remainder when using integer division.

-> enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other
object which supports iteration.

-> eval(expression[, globals[, locals]])
The arguments are a string and optional globals and locals. If provided, globals must be
a dictionary. If provided, locals can be any mapping object.

-> exec(object[, globals[, locals]])
This function supports dynamic execution of Python code. object must be either a string
or a code object. If it is a string, the string is parsed as a suite of Python
statements which is then executed (unless a syntax error occurs).

-> filter(function, iterable)
Construct an iterator from those elements of iterable for which function returns true.
iterable may be either a sequence, a container which supports iteration, or an iterator.
If function is None, the identity function is assumed, that is, all elements of iterable
that are false are removed.

-> class float([x])
Return a floating point number constructed from a number or string x.
If the argument is a string, it should contain a decimal number, optionally preceded
by a sign, and optionally embedded in whitespace.

-> format(value[, format_spec])
Convert a value to a "formatted" representation, as controlled by format_spec. The
interpretation of format_spec will depend on the type of the value argument, however
there is a standard formatting syntax that is used by most built-in types.

-> class frozenset([iterable])
Return a new frozenset object, optionally with elements taken from iterable.
frozenset is a built-in class.

-> getattr(object, name[, default])
Return the value of the named attribute of object. name must be a string. If the string
is the name of one of the object's attributes, the result is the value of that attribute.
e.g. getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does
not exist, default is returned if provided, otherwise AttributeError is raised.

-> globals()
Return a dictionary representing the current global symbol table. This is always the
dictionary of the current module (inside a function or method, this is the module where
it is defined, not the module from which it is called).
"""
