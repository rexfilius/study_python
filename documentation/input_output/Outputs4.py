# Basic usage of the str.format() method looks like this
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# The brackets and characters within them (called format fields) are replaced with the
# objects passed into the str.format() method. A number in the brackets can be used
# to refer to the position of the object passed into the str.format() method.
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print()

# If keyword arguments are used in the str.format() method, their values are referred
# to by using the name of the argument.
print('This {food} is {comment}.'.format(food='egg', comment='absolutely horrible'))

# Positional and keyword arguments can be arbitrarily combined.
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print()

# If you have a really long format string that you don't want to split up, it would
# be nice if you could reference the variables to be formatted by name instead of
# by position. This can be done by simply passing the dict and using square brackets
# '[]' to access the keys.
girls_table = {'Simi': 4127, 'Mimi': 4098, 'Jane': 8637}
print('Mimi: {0[Mimi]:d}; Simi: {0[Simi]:d}; '
      'Jane: {0[Jane]:d}'.format(girls_table))

# This could also be done by passing the table as keyword arguments with
# the '**' notation.
print('Mimi: {Mimi:d}; Simi: {Simi:d}; '
      'Jane: {Jane:d}'.format(**girls_table))
print()

# This is particularly useful in combination with the built-in function vars(),
# which returns a dictionary containing all local variables.
# As an example, the code below produce a tidily-aligned set of columns giving
# integers and their squares and cubes
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
