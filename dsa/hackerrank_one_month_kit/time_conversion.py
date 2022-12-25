"""
Given a time in AM/PM format, convert it to military (24-hour) time.
Note: 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

input1 = 12:01:00PM
output1 = 12:01:00

input2 = 07:05:45PM
output2 = 19:05:45

explain ---
1.00.00PM => 13.00.00
01.00.00AM => 01.00.00

ALGO::
-> 07 : 05 : 45 PM
-> 01 2 34 5 67 89 -> indices
Get string in PM/AM format
- If string is PM; string[8:10] equal PM
    - get the first 2 chars as int
    - if the chars is 12, return "string[0:8]"
    - if the chars is less than 12, add 12 to it, return 'int+12' + string[2:8]
- If string is AM; string[8:10] equal AM
    - get the first 2 chars as int
    - if the chars is 12, return '00' + string[2:8]
    - if the chars is less than 12, return "string[0:8]
"""


def timeConversion(timeString: str):
    timeFormat = str(timeString[8:10])  # PM or AM
    hourTime = int(timeString[0:2])
    if timeFormat == 'PM':
        if hourTime == 12:
            return timeString[0:8]
        elif hourTime < 12:
            return f'{hourTime + 12}' + timeString[2:8]
    elif timeFormat == 'AM':
        if hourTime == 12:
            return '00' + timeString[2:8]
        elif hourTime < 12:
            return timeString[0:8]


print(timeConversion('01:00:00AM'))
