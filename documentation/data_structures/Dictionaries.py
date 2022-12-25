"""
Dictionaries are sometimes found in other languages as "associative memories" or
"associative arrays".

Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys.

Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple
contains any mutable object either directly or indirectly, it cannot be used as a key.

You can't use lists as keys, since lists can be modified in place using index
assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as a set of 'key:value pairs', with the requirement
that the keys are unique (within one dictionary).

A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of
key:value pairs within the braces adds initial key:value pairs to the dictionary;
this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting
the value given the key. It is also possible to delete a key:value pair with del.

If you store using a key that is already in use, the old value associated with that
key is forgotten. It is an error to extract a value using a non-existent key.

Performing list(d) on a dictionary returns a list of all the keys used in the
dictionary, in insertion order (if you want it sorted, just use sorted(d) instead).
To check whether a single key is in the dictionary, use the in keyword.
"""
phone_contact = {'bane': 7654, 'jack': 4098, 'jane': 4139}
print(phone_contact)

phone_contact['timi'] = 7683
phone_contact['mimi'] = 9802
phone_contact['kiki'] = 9354
print(phone_contact)
print()

print(phone_contact['jack'])  # ans  = 4098
del phone_contact['kiki']
print(phone_contact)
print()

print(list(phone_contact))
print(sorted(phone_contact))
print()

print('mimi' in phone_contact)
print('jane' not in phone_contact)
print()
