"""
-> hasattr(object, name)
The arguments are an object and a string. The result is True if the string is the name
of one of the object's attributes, False if not. (This is implemented by calling
getattr(object, name) and seeing whether it raises an AttributeError or not.)

-> hash(object)
Return the hash value of the object (if it has one). Hash values are integers.

-> help([object])
Invoke the built-in help system. (This function is intended for interactive use.)
If no argument is given, the interactive help system starts on the interpreter console.
If the argument is a string, then the string is looked up as the name of a module,
function, class, method, keyword, or documentation topic, and a help page is printed
on the console. If the argument is any other kind of object, a help page on the object
is generated.

-> hex(x)
Convert an integer number to a lowercase hexadecimal string prefixed with "0x".
If x is not a Python int object, it has to define an __index__() method that
returns an integer.

-> id(object)
Return the "identity" of an object. This is an integer which is guaranteed to be unique
and constant for this object during its lifetime. Two objects with non-overlapping
lifetimes may have the same id() value.

-> input([prompt])
If the prompt argument is present, it is written to standard output without a trailing
newline. The function then reads a line from input, converts it to a string
(stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.

-> class int([x])
-> class int(x, base=10)
Return an integer object constructed from a number or string x,
or return 0 if no arguments are given.

-> isinstance(object, classinfo)
Return True if the object argument is an instance of the classinfo argument, or of a
(direct, indirect or virtual) subclass thereof. If object is not an object of the given
type, the function always returns False. If classinfo is a tuple of type objects
(or recursively, other such tuples), return True if object is an instance of any of
the types. If classinfo is not a type or tuple of types and such tuples,
a TypeError exception is raised.

-> issubclass(class, classinfo)
Return True if class is a subclass (direct, indirect or virtual) of classinfo. A class
is considered a subclass of itself. classinfo may be a tuple of class objects, in which
case return True if class is a subclass of any entry in classinfo. In any other case,
a TypeError exception is raised.

-> iter(object[, sentinel])
Return an iterator object

-> len(s)
Return the length (the number of items) of an object. The argument may be a sequence
(such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary,
set, or frozen set).
"""