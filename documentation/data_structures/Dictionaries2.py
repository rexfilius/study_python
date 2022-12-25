# The dict() constructor builds dictionaries directly from
# sequences of key-value pairs.
dict_one = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict_one)

# In addition, dict comprehensions can be used to create dictionaries
# from arbitrary key and value expressions
dict_two = {x: x ** 2 for x in (2, 4, 6)}
print(dict_two)

# When the keys are simple strings, it is sometimes easier to specify pairs using
# keyword arguments:
dict_three = dict(sape=4139, guido=4127, jack=4098)
print(dict_three)
