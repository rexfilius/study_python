"""
Write a function that returns an array of all anagrams of a given string.
An anagram is a reordering of all the characters within a string.
input = "abc"
output = ["abc", "acb", "bac", "bca", "cab", "cba"]
"""


def anagrams(string):
    """not working as expected
    time complexity is O(N!) - Factorial Time"""
    if len(string) == 1:
        return string[0]
    collection = []
    subStringAnagrams = anagrams(string[1:len(string)])

    for subStringAnagram in subStringAnagrams:
        for index in range(len(subStringAnagram)):
            copy = subStringAnagram[index]
            collection.append(copy)  # or copy[index]
    return collection


# Compare two strings side by side. Return true if they're anagrams of
# each other, and false if they're not.
def anagrams_2(firstString, secondString):
    """O(N*M) Time."""
    secondStringArray = list(secondString)
    for i in range(0, len(firstString)):
        if len(secondStringArray) == 0:
            return False
        for j in range(0, len(secondStringArray)):
            if firstString[i] == secondStringArray[j]:
                del secondStringArray[j]
                break
    # The two strings are only anagrams if the secondStringArray has no characters
    # remaining by the time we're done iterating over the firstString.
    return len(secondStringArray) == 0


# A BETTER VERSION OF anagrams_2(). This algorithm converts each string into a
# hash table that tallies the count of each type of character. Once we've converted
# the two strings into two hash tables, all that's left is to compare the two hash
# tables. If they're identical, it means the two strings are anagrams.
def anagrams_3(firstString, secondString):
    """O(N+M) Time."""
    firstHashTable = {}
    secondHashTable = {}
    for char in firstString:
        if firstHashTable.get(char):
            firstHashTable[char] += 1
        else:
            firstHashTable[char] = 1
    for char in secondString:
        if secondHashTable.get(char):
            secondHashTable[char] += 1
        else:
            secondHashTable[char] = 1
    # the two strings are anagrams only if the two hash tables are identical
    return firstHashTable == secondHashTable


string1 = 'rattles'
string2 = 'startle'
string3 = 'starlet'
string4 = 'startup'
print(anagrams_3(string1, string4))
