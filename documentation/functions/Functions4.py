# Functions can also be called using keyword arguments of the form "kwarg=value".
# KEYWORD ARGUMENT: an argument preceded by an identifier (e.g. name=)
# in a function call or passed as a value in a dictionary preceded by **
# POSITIONAL ARGUMENT: an argument that is not a keyword argument.
# Positional arguments can appear at the beginning of an argument list
# and/or be passed as elements of an iterable preceded by *

# e.g the function below accepts one required argument (voltage) and three optional
# arguments (state, action, and type).
def parrot(voltage, state='stiff', action='fly', birdType='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", birdType)
    print("-- It's", state, "! \n")


# The parrot function CAN BE called in any of the following ways:
parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='leap')  # 2 keyword arguments
parrot(action='hop', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# MY TAKE:::
# [1] when defining a function, you have required argument & optional arguments
# optional arguments have default values
# [2] When calling a function, you have keyword arguments & positional arguments

# The parrot function CANNOT BE called in any of the following ways:
"""
parrot()  # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)  # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""

# In a function call, keyword arguments must follow positional arguments.
# All the keyword arguments passed must match one of the arguments accepted by
# the function and their order is not important.
# This also includes non-optional arguments.
