# List methods
fruit_bag = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruit_bag.count('apple'))  # ans = 2
print(fruit_bag.count('tangerine'))  # ans = 0

print(fruit_bag.index('banana'))  # ans = 3
print(fruit_bag.index('banana', 4))  # Find next banana starting at position 4, ans = 6
print()

fruit_bag.reverse()
print(fruit_bag)

fruit_bag.append('grape')
print(fruit_bag)
print()

fruit_bag.sort()
print(fruit_bag)

print(fruit_bag.pop())

# Methods like insert, remove or sort that only modify the list have no return value
# printed – they return the default None.
# This is a design principle for all mutable data structures in Python.
