"""
-> class list([iterable])
Rather than being a function, list is actually a mutable sequence type.

-> locals()
Update and return a dictionary representing the current local symbol table

-> map(function, iterable, ...)
Return an iterator that applies function to every item of iterable,
yielding the results.

-> max(iterable, *[, key, default])
-> max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.

-> class memoryview(object)
Return a “memory view” object created from the given argument.

-> min(iterable, *[, key, default])
-> min(arg1, arg2, *args[, key])
Return the smallest item in an iterable or the smallest of two or more arguments.

-> next(iterator[, default])
Retrieve the next item from the iterator by calling its __next__() method. If default is
given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

-> class object
Return a new featureless object. object is a base for all classes. It has the methods
that are common to all instances of Python classes. This function does not accept any
arguments.
Note:: object does not have a __dict__, so you can't assign arbitrary attributes to an
instance of the object class.

-> oct(x)
Convert an integer number to an octal string prefixed with "0o". The result is a valid
Python expression. If x is not a Python int object, it has to define an __index__()
method that returns an integer.

-> open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
-> closefd=True, opener=None)
Open file and return a corresponding file object. If the file cannot be opened,
an OSError is raised.

-> ord(c)
Given a string representing one Unicode character, return an integer representing the
Unicode code point of that character. e.g ord('a') returns the integer 97 and
ord('€') (Euro sign) returns 8364. This is the inverse of chr().

-> pow(base, exp[, mod])
Return base to the power exp; if mod is present, return base to the power exp,
modulo mod (computed more efficiently than pow(base, exp) % mod). The two-argument
form pow(base, exp) is equivalent to using the power operator: base**exp.
"""