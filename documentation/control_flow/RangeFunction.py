# If you do need to iterate over a sequence of numbers, the built-in function range()
# comes in handy. It generates arithmetic progressions.
for a in range(5):
    print(a, end='-')
print()

# The given end point in a range() is never part of the generated sequence.
# range(10) generates 10 values, the legal indices for items of a sequence of length 10.
# It is possible to let the range start at another number, or to specify a different
# increment (even negative; sometimes this is called the 'step')
range_list_1 = list(range(5, 10))  # start=5, stop=10, step=null
print(range_list_1)

range_list_2 = list(range(0, 10, 3))  # start=0, stop=10, step=3
print(range_list_2)

range_list_3 = list(range(-10, -100, -30))  # start=-10, stop=-100, step=-30
print(range_list_3)
print()

# To iterate over the indices of a sequence, you can combine range() and len()
presidents = ['Bush', 'Clinton', 'Obama', 'Trump', 'Biden']
for i in range(len(presidents)):
    print(i, presidents[i])

# In most such cases, however, it is convenient to use the enumerate() function
print(list(enumerate(presidents)))

# random - iterating over items as opposed to indices
for president in presidents:
    print(president)
print()
