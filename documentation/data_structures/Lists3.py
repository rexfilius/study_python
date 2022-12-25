# Using Lists as Stacks::
# The list methods make it very easy to use a list as a stack, where the last
# element added is the first element retrieved ("last-in, first-out"). To add
# an item to the top of the stack, use append(). To retrieve an item from the
# top of the stack, use pop() without an explicit index.
stacked = [3, 4, 5]
print(stacked)

stacked.append(6)
stacked.append(7)
print(stacked)

stacked.pop()
print(stacked)
stacked.pop()
print(stacked)
