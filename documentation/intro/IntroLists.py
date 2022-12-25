# Python knows a number of compound data types, used to group together other values.
# The most versatile is the list, which can be written as a list of comma-separated
# values (items) between square brackets. Lists might contain items
# of different types, but usually the items all have the same type.
squared = [1, 4, 9, 16, 25]
print(squared)

# Like strings (and all other built-in sequence types),
# lists can be indexed and sliced
print(squared[-3:])  # slicing returns a new list
print(squared[:])  # returns a shallow copy of the original

# Lists also support operations like concatenation
double_squared = squared + [36, 49, 64, 81, 100]
print(double_squared)
print()

# Unlike strings, which are immutable, lists are a mutable type,
# i.e. it is possible to change their content.
cubed = [1, 8, 27, 65, 125]
cubed[3] = 64
print(cubed)

# You can also add new items at the end of the list, by using the append() method
cubed.append(216)
cubed.append(7 ** 3)
print(cubed)
