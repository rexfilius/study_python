"""
Given an integer n , find each x such that 
1. 0 <= x <= n
2. n + x  = n xor x
@return the number of x's satisfying the criteria

A       B       A XOR B
False   False   False
False   True    True
True    False   True
True    True    False

EXAMPLE::
n = 4           (0100)
4 + 0 = 4 xor 0 (0000) = 4 (0100)
4 + 1 = 4 xor 1 (0001) = 5 (0101)
4 + 2 = 4 xor 2 (0010) = 6 (0110)
4 + 3 = 4 xor 3 (0011) = 7 (0111)
output = 4

ALGO::
paramter = n
nInBinary = bin(n)
for i in 0 to n
    - numberInBinary = bin(i)
    - xorOp = int(nInBinary) ^ int(numberInBinary)
    - if xorOp == n + i; count++
"""


def sumXor(n: int):
    count = 0
    nInBinary = bin(n)
    for i in range(n + 1):
        numberInBinary = bin(i)
        xorOp = int(nInBinary, base=2) ^ int(numberInBinary, base=2)
        if xorOp == n + i:
            count += 1
    return count


def sumXor_2(n: int):
    """Passed all HackerRank Test cases"""
    zeroCount = bin(n)[2:].count('0')
    if n == 0:
        return 1
    else:
        return 2 ** zeroCount
    # return 1 if n == 0 else 2 ** (bin(n)[2:].count('0'))


print(sumXor_2(10))
# print(bin(3))
# print(int('0b0111', base=2))
