import math

"""
Formatted string literals (also called f-strings for short) let you include the value 
of Python expressions inside a string by prefixing the string with 'f' or 'F' and 
writing expressions as {expression}.

An optional format specifier can follow the expression. This allows greater control 
over how the value is formatted.
"""

# The following example rounds pi to three places after the decimal:
print(f'The value of pi is approximately {math.pi:.3f}.')
print()

# Passing an integer after the ':' will cause that field to be a minimum number of
# characters wide. This is useful for making columns line up.
x_table = {'Simi': 4127, 'Jack': 4098, 'Drew': 7678}
for name, phone in x_table.items():
    print(f'{name:10} ==> {phone:10d}')
print()

# Other modifiers can be used to convert the value before it is formatted.
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
these_animals = 'eels'
print(f'My hovercraft is full of {these_animals}.')
print(f'My hovercraft is full of {these_animals!r}.')
