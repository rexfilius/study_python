# Finally, the least frequently used option is to specify that a function can be 
# called with an arbitrary number of arguments. These arguments will be wrapped up 
# in a tuple. Before the variable number of arguments, 
# zero or more normal arguments may occur.
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# Normally, these 'variadic' arguments will be last in the list of formal parameters,
# because they scoop up all remaining input arguments that are passed to the function.
# Any formal parameters which occur after the *args parameter are 'keyword-only'
# arguments, meaning that they can only be used as keywords
# rather than positional arguments.
def concat(*args, sep='/'):
    return sep.join(args)


concat_1 = concat("earth", "mars", "venus")
print(concat_1)
concat_2 = concat('earth', 'mars', 'venus', sep='-')
print(concat_2)
print()

# UNPACKING ARGUMENT LISTS
# The reverse situation occurs when the arguments are already in a list or tuple
# but need to be unpacked for a function call requiring separate positional arguments.
# e.g. the built-in range() function expects separate start and stop arguments.
# If they are not available separately, write the function call with the * -operator
# to unpack the arguments out of a list or tuple
unpack = list(range(3, 6))
print(unpack)

unpack_args = [3, 6]
unpack_2 = list(range(*unpack_args))
print(unpack_2)
print()


# In the same fashion, dictionaries can deliver keyword arguments with the ** operator
def parrot_2(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot_2(**d)
