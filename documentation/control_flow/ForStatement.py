# In 'for' statement in Python, rather than always iterating over an arithmetic
# progression of numbers (like in Pascal), or giving the user the ability to define
# both the iteration step and halting condition (as C),
# Python's for statement iterates over the items of any sequence (a list or a string),
# in the order that they appear in the sequence.
caged_animals = ['dog', 'duck', 'deer']
for animal in caged_animals:
    print(animal, len(animal))

# Code that modifies a collection while iterating over that same collection can be
# tricky to get right. Instead, it is usually more straight-forward to loop over
# a copy of the collection or to create a new collection.
"""
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
"""
