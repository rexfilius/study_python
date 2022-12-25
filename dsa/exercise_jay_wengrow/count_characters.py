"""
Write a function that returns the number of 'x' in a given string.
input = "axbxcxd"
output = 3
"""


def countCharacters(string, character='x'):
    if len(string) == 0:
        return 0
    if string[0] == character:
        return 1 + countCharacters(string[1:len(string)], character=character)
    else:
        return countCharacters(string[1:len(string)], character=character)


print(countCharacters('axbxcxd', 'x'))
print(countCharacters('ifeakachukwu', character='k'))
print(countCharacters('mississippi', character='s'))

# stry = 'ade'
# print(len(stry[1:0]) == 0)  # answer = True
