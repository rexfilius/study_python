"""
The Python interpreter has a number of functions and types built into it that are
always available.

-> abs(x)
Return the absolute value of a number. The argument may be an integer, a floating point
number, or an object implementing __abs__(). If the argument is a complex number,
its magnitude is returned.

-> all(iterable)
Return True if all elements of the iterable are true (or if the iterable is empty).

-> any(iterable)
Return True if any element of the iterable is true.
If the iterable is empty, return False.

-> ascii(object)
As repr(), return a string containing a printable representation of an object,
but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U
escapes. This generates a string similar to that returned by repr() in Python 2.

-> bin(x)
Convert an integer number to a binary string prefixed with "0b". The result is a valid
Python expression. If x is not a Python int object, it has to define an __index__()
method that returns an integer.

-> class bool([x])
Return a Boolean value, i.e. one of True or False. x is converted using the standard
truth testing procedure. If x is false or omitted, this returns False; otherwise
it returns True. The bool class is a subclass of int.
It cannot be subclassed further. Its only instances are False and True.
Changed in version 3.7: x is now a positional-only parameter.

-> breakpoint(*args, **kws)
This function drops you into the debugger at the call site. Specifically, it calls
sys.breakpointhook(), passing args and kws straight through. By default,
sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case,
it is purely a convenience function so you don’t have to explicitly import pdb or
type as much code to enter the debugger. However, sys.breakpointhook() can be set
to some other function and breakpoint() will automatically call that, allowing you
to drop into the debugger of choice.

-> class bytearray([source[, encoding[, errors]]])
Return a new array of bytes. The bytearray class is a mutable sequence of integers in
the range 0 <= x < 256. It has most of the usual methods of mutable sequences.

The optional source parameter can be used to initialize the array in a few different
ways:
- If it is a string, you must also give the encoding (and optionally, errors)
parameters; bytearray() then converts the string to bytes using str.encode().
- If it is an integer, the array will have that size and will be initialized with
null bytes.
- If it is an object conforming to the buffer interface, a read-only buffer of the
object will be used to initialize the bytes array.
- If it is an iterable, it must be an iterable of integers in the range 0 <= x < 256,
which are used as the initial contents of the array.
Without an argument, an array of size 0 is created.
"""
