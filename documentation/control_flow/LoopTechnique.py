import math

# When looping through dictionaries, the key and corresponding value can be retrieved
# at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
print()

# When looping through a sequence, the position index and corresponding value can be
# retrieved at the same time using the enumerate() function.
tic_toe = ['tic', 'tac', 'toe']
for i, v in enumerate(tic_toe):
    print(i, v)
print()

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
print()

# To loop over a sequence in reverse, first specify the sequence in a forward
# direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)
print()

# To loop over a sequence in sorted order, use the sorted() function which returns
# a new sorted list while leaving the source unaltered.
fruity_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(fruity_list):
    print(i)
print()

# Using set() on a sequence eliminates duplicate elements. The use of sorted()
# in combination with set() over a sequence is an idiomatic way to loop over
# unique elements of the sequence in sorted order.
fruity_list_2 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(fruity_list_2)):
    print(f)
print()

# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead.
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
