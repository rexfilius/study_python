# It is also possible to define functions with a variable number of arguments.
# There are three forms, which can be combined.
# 1. Default Argument Values
# 2. Keyword Arguments
# 3. Special Parameters
# 4. Arbitrary Argument List

# The most useful form is to specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments than it is
# defined to allow.
# SIDE NOTE: The 'in' keyword tests whether or not a sequence contains a certain value.
def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# The ask_ok function above can be called in several ways
# 1. giving the only mandatory argument
ask_ok('Do you really want to quit')
# 2. giving one of the optional arguments
ask_ok('Ok to overwrite the file?', 2)
# 3. giving all the arguments
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
