"""
A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either 'pangram' or 'not pangram' as appropriate.

s1 = 'The quick brown fox jumps over the lazy dog'
output = 'pangram'; the string contains every alphabet

s2 = 'We promptly judged antique ivory buckles for the next prize'
output = 'pangram'

s3 = 'We promptly judged antique ivory buckles for the prize'
output = 'not pangram'

ALGO::
alphabets = 'abcdefghijklmnopqrstuvwxyz'
convert sentence to lower case.
for char in sentence:
    - if char is whitespace, continue
    - else hashTable[char] = True
for letter in alphabets:
    - if hashTable.get(letter) is None, return 'not pangram'
@return 'pangram'
"""


def pangram(sentence: str):
    hashTable = {}
    lowercaseString = sentence.lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for char in lowercaseString:
        if char == ' ':
            continue
        else:
            hashTable[char] = True
    for letter in alphabets:
        if hashTable.get(letter) is None:
            return 'not pangram'
    return 'pangram'


s1 = 'The quick brown fox jumps over the lazy dog'  # pangram
s2 = 'We promptly judged antique ivory buckles for the next prize'  # pangram
s3 = 'We promptly judged antique ivory buckles for the prize'  # not pangram
print(pangram(s3))
