"""
-> class str(object='')
-> class str(object=b'', encoding='utf-8', errors='strict')
Return a str version of object. str is the built-in string class

-> sum(iterable, /, start=0)
Sums start and the items of an iterable from left to right and returns the total. The
iterable's items are normally numbers, and the start value is not allowed to be a
string.
For some use cases, there are good alternatives to sum(). The preferred, fast way to
concatenate a sequence of strings is by calling ''.join(sequence). To add floating
point values with extended precision, see math.fsum(). To concatenate a series of
iterables, consider using itertools.chain().

-> super([type[, object-or-type]])
Return a proxy object that delegates method calls to a parent or sibling class of type.
This is useful for accessing inherited methods that have been overridden in a class.

-> class tuple([iterable])
Rather than being a function, tuple is actually an immutable sequence type.

-> class type(object)
-> class type(name, bases, dict, **kwds)
With one argument, return the type of an object. The return value is a type object and
generally the same object as returned by object.__class__.

The isinstance() built-in function is recommended for testing the type of an object,
because it takes subclasses into account.

-> vars([object])
Return the __dict__ attribute for a module, class, instance, or any other object
with a __dict__ attribute.

-> zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.
"""
