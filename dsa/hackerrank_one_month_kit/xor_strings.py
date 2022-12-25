"""
Given two strings consisting of digits 0 and 1 only,
find the XOR of the two strings.

input1 = 10101 and 00101
output1 = 10000
@return: string obtained by the XOR of the two input strings.

EXPLAINING XOR::
A       B       A xor B
False   False   False
False	True	True
True	False	True
True	True	False

ALGO::
parameters: s1, s2 => both are strings
variable: xorString
for index in range(len(s1))
    - if s1[index] == s2[index], xorString += '0'
    - else xorString += '1'
"""


def xorString(s1: str, s2: str):
    xorStr = ''
    for index in range(len(s1)):
        if s1[index] == s2[index]:
            xorStr += '0'
        else:
            xorStr += '1'
    return xorStr


print(xorString('10101', '00101'))  # answer = 10000
print(xorString('01010', '10101'))  # answer = 11111
