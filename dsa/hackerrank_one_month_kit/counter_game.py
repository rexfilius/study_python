"""
Louise and Richard have developed a numbers game. They pick a number and check to
see if it is a power of 2. If it is, they divide it by 2. If not, they reduce it
by the next lower number which is a power of 2. Whoever reduces the number to 1
wins the game. Louise always starts.
Given an initial value, determine who wins the game.
@return - string: either 'Richard' or 'Louise'

EXAMPLE::
n = 132
It's Louise's turn first. She determines that 132 is not a power of 2.
The next lower power of 2 is 128, so she subtracts that from 132 and passes 4
to Richard. 4 is a power of 2, so Richard divides it by 2 and passes 2 to Louise.
Likewise, 2 is a power, so she divides it by 2 and reaches 1. She wins the game.
NOTE - If they initially set counter to 1, Richard wins.
Louise cannot make a move so she loses.

EXPLAINING::
(if n is a power of 2, divide; else minus by next lower power of 2)
n = 132
132 is not a power of 2
Louise minus 128; n is 4  => 4 invexp of 2 is 2
Richard divides by 2; n is 2
Louise divides by 2; n is 1 - Louise wins

n = 6
6 is not a power of 2
Louise minus 4; n is 2  => 2 invexp of 2 is 1
Richard divides by 2; n is 1 - Richard wins

n = 15
15 is not a power of 2
Louise minus 8; n is 7
Richard minus 4; n is 3
Luise minus 2; n is 1 - Louise wins

n = 35
35 is not a power of 2
Louise minus 32; n is 3
Richard minus 2; n is 1 - Richard wins

n = 16
16 is a power of 2
Louise divides by 2; n is 8
Richard divides by 2; n is 4
Louise divides by 2; n is 2
Richard divides by 2; n is 1 - Richard wins

n = 1024 (1024 inverse exp of 2 = 10)
1024 is a power of 2
Louise divides by 2; n is 512
Richard divides by 2; n is 256
Louise divides by 2; n is 128
Richard divides by 2; n is 64
Louise divides by 2; n is 32
Richard divides by 2; n is 16
Louise divides by 2; n is 8
Richard divides by 2; n is 4
Louise divides by 2; n is 2
Richard divides by 2; n is 1 - Richard wins

n = 32 (32 inverse exp of 2 = 5)
Louise divides by 2; n is 16
Richard divides by 2; n is 8
Louise divides by 2; n is 4
Richard divides by 2; n is 2
Louise divides by 2; n is 1 - Louise wins

ALGO::

"""


def counterGame(n):
    """SAW THE SOLUTION IN HACKERRANK DISCUSSIONS
    I STILL DO NOT UNDERSTAND THE ALGORITHM"""
    pass
