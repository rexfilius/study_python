# List comprehensions provide a concise way to create lists. Common applications are
# to make new lists where each element is the result of some operations applied
# to each member of another sequence or iterable, or to create a subsequence
# of those elements that satisfy a certain condition.
# e.g. assume we want to create a list of squares, like:
squares_one = []
for x in range(10):
    squares_one.append(x ** 2)

print(squares_one)

# Note that this creates (or overwrites) a variable named x that still exists after
# the loop completes. We can calculate the list of squares without any side effects
squares_two = list(map(lambda y: y ** 2, range(10)))
print(squares_two)

# writing the code above to be more concise and readable
squares_three = [x ** 2 for x in range(10)]
print(squares_three)
print()

# A LIST COMPREHENSION consists of brackets containing an expression followed by a
# 'for' clause, then zero or more 'for' or 'if' clauses.
# The result will be a new list resulting from evaluating the expression in the
# context of the for and if clauses which follow it.

# the list comprehension below combines the elements of two lists if they aren't equal
comb_one = [(a, b) for a in [1, 2, 3] for b in [3, 1, 4] if a != b]
print(comb_one)
# and this is equivalent to the code below
comb_two = []
for c in [1, 2, 3]:
    for d in [3, 1, 4]:
        if c != d:
            comb_two.append((c, d))

print(comb_two)
