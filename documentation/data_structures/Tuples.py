# Sequence types in Python - list, tuple, range
# A tuple consists of a number of values separated by commas
# Tuples may be nested. They are immutable but they can contain mutable objects
tuple_1 = 12345, 54321, 'Hello'
print(tuple_1[0])
print(tuple_1)

tuple_2 = tuple_1, (1, 2, 3, 4, 5)
print(tuple_2)

# tuple_1[0] = 8888  !!Error!!

tuple_3 = ([1, 2, 3], [3, 2, 1])
print(tuple_3)
print()

"""
On output, tuples are always enclosed in parentheses, so that nested tuples are 
interpreted correctly; they may be input with or without surrounding parentheses, 
although often parentheses are necessary anyway (if the tuple is part of a larger 
expression). It is not possible to assign to the individual items of a tuple, 
however it is possible to create tuples which contain mutable objects, such as lists.

Though tuples may seem similar to lists, they are often used in different situations 
and for different purposes. Tuples are immutable, and usually contain a heterogeneous
sequence of elements that are accessed via unpacking or indexing 
(or even by attribute in the case of namedtuples). Lists are mutable, and their 
elements are usually homogeneous and are accessed by iterating over the list.
"""
