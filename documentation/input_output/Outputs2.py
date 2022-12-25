"""
When you don't need fancy output but just want a quick display of some variables
for debugging purposes, you can convert any value to a string with the
repr() or str() functions.

The str() function is meant to return representations of values which are fairly
human-readable, while repr() is meant to generate representations which can be read
by the interpreter (or will force a SyntaxError if there is no equivalent syntax).

For objects which don't have a particular representation for human consumption,
str() will return the same value as repr(). Many values, such as numbers or structures
like lists and dictionaries, have the same representation using either function.
Strings, in particular, have two distinct representations.
"""
s_t = 'hello world'
print(str(s_t))
print(repr(s_t))

# The string module contains a Template class that offers yet another way to substitute
# values into strings, using placeholders like $x and replacing them with values
# from a dictionary, but offers much less control of the formatting.
