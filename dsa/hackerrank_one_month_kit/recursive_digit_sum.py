"""
We define super digit of an integer x using the following rules:
Given an integer, we need to find the super digit of the integer.
1. If x has only 1 digit, then its super digit is x.
2. Otherwise, the super digit of x is equal to the super digit of the sum
of the digits of x.

EXAMPLE::
super-digit of 9875 = 9+8+7+5 = 29
super-digit of 29 = 2+9 = 11
super-digit of 11 = 1+1
super-digit of 2 = 2

EXAMPLE CASE::
n = '9875' and k = 4
p = 9875987598759875
p is created by concatenating the string n, k times.
superDigit(p) = 9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
superDigit(116) = 1+1+6 = 8
superDigit(8) = 8
output = 8; is the super digit

n = '148' and k = 3
p = 148148148
super-digit of p = 1+4+8+1+4+8+1+4+8 = 39
super-digit of 39 = 3+9 = 12
super-digit of 12 = 1+2 = 3
super-digit of 3 = 3
output = 3

n = '123' and k = 3
p = 123123123
super-digit(p) = 1+2+3+1+2+3+1+2+3 = 18
super-digit(18) = 1+8 = 9
super-digit(9) = 9
output = 9

ALGO:
parameter, n: String and k: Int
nList = [int(val) for val in str(n*k)]
sumOfDigit = sum(nList)
if len(str(sumOfDigit)) == 1:
    - return sumOfDigit
else
    - return superDigit(n=sumOfDigit, k =1)
"""


def superDigit(n: str, k: int):
    nlist = [int(val) for val in str(n * k)]
    sumOfDigit = sum(nlist)
    if len(str(sumOfDigit)) == 1:
        return sumOfDigit
    else:
        return superDigit(str(sumOfDigit), 1)


def superDigit_2(n: str, k: int):
    """from HackerRank discussions"""
    if len(n) == 1 and k == 1:
        return n
    nlist = [int(d) for d in n]
    total = str(sum(nlist) * k)
    return superDigit(total, 1)


print(superDigit('9875', 4))
print(superDigit('148', 3))
print(superDigit('123', 3))
