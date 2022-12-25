"""
Given a list of 32-bit unsigned integers. Flip all the bits(1->0 and 0->1)
and return the result as an unsigned integer.

EXAMPLE::
n = 9 (in base10)
9 = 1001 (in base2); we're working with 32-bit so;
00000000000000000000000000001001 = 9
11111111111111111111111111110110 = 4294967286
@return 4294967286
"""


def flippingBits(n):
    """got solution from HackerRank discussions"""
    numberInBinary = bin(n)
    numberIn32BitBin = numberInBinary[2:].zfill(32)
    container = ''
    for value in numberIn32BitBin:
        if value == '1':
            container += '0'
        else:
            container += '1'
    result = int(container, base=2)
    return result


def flippingBits_2(n):
    """got solution from HackerRank discussions"""
    return ((2 ** 32) - 1) - n


print(flippingBits(10))
print(flippingBits_2(10))
