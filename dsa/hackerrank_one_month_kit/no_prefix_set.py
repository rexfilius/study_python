"""
There is a given list of strings where each string contains only lowercase letters from a to j, inclusive.
The set of strings is said to be a GOOD SET if no string is a prefix of another string.
In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.
Note - If two strings are identical, they are prefixes of each other.

EXAMPLE::
words = ['abcd', 'bcd', 'abcde', 'bcde']
output = BAD SET; abcde

words = ['ab', 'bc', 'cd']
output = GOOD SET

words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
output = BAD SET; aabcde

words = ['aab', 'aac, 'aacghgh', 'aabghgh']
output = BAD SET; aacghgh

ALGO::
THIS PROBLEM SEEMS LIKE IT CAN BE BETTER SOLVED WITH A TRIE DATA STRUCTURE.
I DO NOT UNDERSTAND TRIE YET. I COPIED AND PASTED THE TWO SOLUTIONS FROM HACKERRANK DISCUSSIONS.
"""


def noPrefix(words):
    partial, full = set(), set()

    for w in words:
        if w in partial:
            print(f"BAD SET\n{w}")
            return
        for i in range(1, len(w) + 1):
            if w[:i] in full:
                print(f"BAD SET\n{w}")
                return
            partial.add(w[:i])
        full.add(w)
    print("GOOD SET")


def noPrefix2(words):
    intermediate_prefixes = {}
    prefixes = {}
    for word in words:
        if word in intermediate_prefixes:
            print("BAD SET")
            print(word)
            return
        for i in range(0, len(word) + 1):
            intermediate_prefixes[word[0:i]] = 0
            if word[0:i] in prefixes:
                print("BAD SET")
                print(word)
                return
        prefixes[word] = 0
    print("GOOD SET")
