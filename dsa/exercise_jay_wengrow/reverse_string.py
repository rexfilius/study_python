from algoJayWengrow.stack.MyStack import MyStack

"""
Write a function that uses a stack to reverse a string.
input = "abcde"
output = "edcba"
"""


def reverseString_stack(string):
    stack = MyStack()
    reversedString = ''
    for character in string:
        stack.push(character)
    for i in range(len(stack)):
        reversedString += stack.pop()
    return reversedString


def reverseString_list(string):
    sList = []
    reversedString = ''
    for character in string:
        sList.append(character)
    for i in range(len(sList)):
        reversedString += sList.pop()
    return reversedString


def reverseString_builtin(string):
    reversedString = ''
    for character in reversed(string):
        reversedString += character
    return reversedString


def reverseString_recurse(string):
    if len(string) == 1:
        return string[0]
    return reverseString_recurse(string[1:len(string)]) + string[0]


print(reverseString_stack("abcde"))
print(reverseString_list("abcde"))
print(reverseString_builtin("abcde"))
print(reverseString_recurse("abcde"))
