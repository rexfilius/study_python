"""
Sherlock considers a string to be valid if all characters of the string appear the
same number of times. It is also valid if he can remove just 1 character at 1 index
in the string, and the remaining characters will occur the same number of times.
Given a string s, determine if it is valid. If so, return YES, otherwise return NO.

EXAMPLE::
s = abc => len is 3
a=1 b=2 c=1
output = YES; it is valid

s = abcc => len is 4
a=1 b=1 c=2
output = YES; if one c is removed, the remaining occur once

s = abccc => len is 5
a=1 b=1 c=3
output = NO; if one c is removed, the remaining occurences are imbalanced

s = aabbcd => len is 6
a=2 b=2 c=1 d=1
output = NO; remove a or b, remaining occurence is imbalanced

s = aabbccddeefghi => len is 14
a=2 b=2 c=2 d=2 e=2 f=1 g=1 h=1 i=1
output = NO

s = abcdefghhgfedecba => len is 17
a=2 b=2 c=2 d=2 e=3 f=2 g=2 h=2
output = YES

ALGO::
for char in string
    - if hashTable.get(char); hashTable[char] +=1
    - else hashTable[char] = 1
for value in hashTable.values
    - frequencyList = list.append(value)
minOcc = min(freguencyList)
maxOcc = max(frequencyList)
if minOcc == maxOcc; return 'YES'
"""


def isValid(s):
    strArray = list(s)
    frequency = {}
    for item in strArray:
        if frequency.get(item):
            frequency[item] += 1
        else:
            frequency[item] = 1

    sortedFrequency = sorted(list(frequency.values()))
    maxFreq = sortedFrequency[len(sortedFrequency) - 1]
    minFreq = sortedFrequency[0]

    if maxFreq == sortedFrequency[len(sortedFrequency) - 2]:
        # check min Freq
        res = [i for i in sortedFrequency if i != maxFreq]
        if len(res) > 1:
            return 'NO'
        else:
            return 'YES'
    else:
        if sortedFrequency[len(sortedFrequency) - 2] == minFreq:
            if maxFreq - 1 == minFreq:
                return 'YES'
        return 'NO'
