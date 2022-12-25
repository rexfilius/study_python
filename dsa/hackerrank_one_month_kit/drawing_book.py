"""
A teacher asks the class to open their books to a page number. A student can either
start turning pages from the front of the book or from the back of the book. They
always turn pages one at a time. When they open the book, page 1 is always on the
right side. When they flip page 1, they see pages 2 and 3. Each page except the last
page will always be printed on both sides. The last page may only be printed on the
front, given the length of the book. If the book is n pages long, and a student
wants to turn to page p, what is the minimum number of pages to turn? They can start
at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in
order to arrive at page p.

EXAMPLE::
n= 5
p= 3
output = 1
from front -> -1 2-3 4-5 -> 1 turn
from back -> 4-5 2-3 -1  -> 1 turn

n= 6
p= 2
output = 1
from front -> -1 2-3 4-5 6-  -> 1 turn
from back -> -6 4-5 2-3 -1   -> 2 turn

n= 5
p= 4
output = 0
from front -> -1 2-3 4-5 -> 2 turns
from back -> 4-5 2-3 -1  -> 0 turns

CONSTRAINTS::
1 <= P <= N

ALGO::

"""


def pageCount(n, p):
    """
    Got solution from HackerRank discussion
    :param n: number of pages
    :param p: page number to turn to
    :return:
    """
    # no. of pages to flip to reach page n
    flipsToPageN = n // 2
    # no. of pages to flip to reach p from front
    flipsToPageP = p // 2
    # no. of pages to flip to reach p from back
    flipsFromBack = flipsToPageN - flipsToPageP
    return min(flipsToPageP, flipsFromBack)
