"""
Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. e.g. the string, "the quick
brown box jumps over a lazy dog" contains all letters of the alphabet except "f".
"""


def findMissingLetter(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    hashTable = {}
    for value in string:
        hashTable[value] = True
    for character in alphabets:
        if not hashTable.get(character):
            return character


s1 = 'the quick brown box jumps over a lazy dog'  # f is missing
print('missing letter:', findMissingLetter(s1))
