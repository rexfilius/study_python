"""
Given two dates each in the format dd-mm-yyyy, you have to find the number of
lucky dates between them (inclusive). To see if a date is lucky,
1. Firstly, sequentially concatinate the date, month and year, into a new integer x
erasing the leading zeroes.
2. Now if x is divisible by either 4 or 7, then we call the date a lucky date.

EXAMPLE::
date = 02-08-2024
concatenate, then x = 2082024
x is divisible by 4 so the date is a lucky date
"""

month = []


def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29  # prev 28
    elif year % 100 == 0:
        month[2] = 28  # prev 29
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28


def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31


def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while True:
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1  # prev 1000
        if x % 4 == 0 or x % 7 == 0:  # prev and
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 = y1 + 1
                m1 = 1  # prev m1 = 1
    return result
