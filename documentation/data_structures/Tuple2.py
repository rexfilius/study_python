# A special problem is the construction of tuples containing 0 or 1 items: the syntax
# has some extra quirks to accommodate these. Empty tuples are constructed by an
# empty pair of parentheses; a tuple with one item is constructed by following a value
# with a comma.
empty_tuple = ()
singleton_tuple = 'hello',

print(len(empty_tuple))
print(len(singleton_tuple))
print()

# the statement below is an example of TUPLE PACKING
pack_sample = 440, 419, 'Yahoo'
# the reverse operation is also possible
c, d, e = pack_sample
print(c)

# This is called SEQUENCE UNPACKING and works for any sequence on the right-hand side.
# Sequence unpacking requires that there are as many variables on the left side of the
# equals sign as there are elements in the sequence.
# Note that multiple assignment is really just a combination of tuple packing and
# sequence unpacking.
