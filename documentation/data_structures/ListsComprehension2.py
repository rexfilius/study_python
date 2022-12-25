from math import pi

# More list comprehension examples

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
vec_2 = [x * 2 for x in vec]
print(vec_2)

# # filter the list to exclude negative numbers
vec_3 = [x for x in vec if x >= 0]
print(vec_3)

# apply a function to all the elements
vec_4 = [abs(x) for x in vec]
print(vec_4)
print()

# call a method on each element
fresh_fruits = ['  banana', '  loganberry ', 'passion fruit  ']

fresh_fruits_2 = [weapon.strip() for weapon in fresh_fruits]
print(fresh_fruits_2)
print()

# create a list of 2-tuples like (number, square)
# the tuple must be parenthesized, otherwise an error is raised
number_squared = [(x, x ** 2) for x in range(6)]
print(number_squared)

# flatten a list using a list comprehension with two 'for'
stack_num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
stack_num_2 = [number for element in stack_num for number in element]
print(stack_num_2)
print()

# List comprehensions can contain complex expressions and nested functions:
rah = [str(round(pi, i)) for i in range(1, 6)]
print(rah)
