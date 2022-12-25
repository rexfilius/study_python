# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection,
# difference, and symmetric difference.
# 'Curly braces' or the 'set()' function can be used to create sets.
# Note: to create an empty set you have to use 'set()', not '{}',
# the latter creates an empty dictionary.
basket_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket_set)  # on output, duplicates are removed

# membership testing in Sets
print('orange' in basket_set)  # ans = True
print('crabgrass' in basket_set)  # ans = False
print()

# Demonstrate set operations on unique letters from two words
a_set = set('abracadabra')
b_set = set('alacazam')

print(f"a_set: {a_set}")  # unique letters in a
print(f"b_set: {b_set}")  # unique letters in b

print(f"a - b: {a_set - b_set}")  # letters in a but not in b
print(f"a | b: {a_set | b_set}")  # letters in a or b or both
print(f"a & b: {a_set & b_set}")  # letters in both a and b
print(f"a ^ b: {a_set ^ b_set}")  # letters in a or b but not both
print()

# Similarly to list comprehensions, set comprehensions are also supported:
c_set = {x for x in a_set if x not in 'abc'}
print(c_set)
