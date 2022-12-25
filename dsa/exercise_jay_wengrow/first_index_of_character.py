"""
Use recursion to write a function that accepts a string and returns
the first index that contains a character. For example, the
input : string-"abcdefghijklmnopqrstuvwxyz" charcter-"x"
output = index 23.
To keep things simple, assume the string definitely has at least one "x"


thinking:
if string[0] == 'x', return 0 (first index)
return firstIndex(string[1:len(string), character)
"""


def findFirstIndexInString(string, character='x'):
    if string[0] == character:
        return 0
    else:
        return findFirstIndexInString(string[1:len(string)], character) + 1


print(findFirstIndexInString('abcdef', character='e'))
print(findFirstIndexInString('abcdefghijklmnopqrstuvwxyz', character='x'))
