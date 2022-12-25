"""
When an exception occurs, it may have an associated value, also known as the
exception's argument. The presence and type of the argument depend
on the exception type.

The except clause may specify a variable after the exception name. The variable
is bound to an exception instance with the arguments stored in 'instance.args'.
For convenience, the exception instance defines __str__() so the arguments can
be printed directly without having to reference '.args'.

One may also instantiate an exception first before raising it and add
any attributes to it as desired.
"""
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)
print()


# If an exception has arguments, they are printed as the last part ('detail') of the
# message for unhandled exceptions.

# Exception handlers don't just handle exceptions if they occur immediately in the try
# clause, but also if they occur inside functions that are called (even indirectly)
# in the try clause.
def this_fails():
    return 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
