"""
There is a large pile of socks that must be paired by color. Given an array of
integers representing the color of each sock, determine how many pairs of socks
with matching colors there are.

EXAMPLE::
n = 7
input1 = [1,2,1,2,1,3,2]
one pair of color 1, one of color 2.
three odd socks left, one of each color. The number of pairs is 2
output1 = 2

n = 9
input2 = [10 20 20 10 10 30 50 10 20]
output2 = 3

n = 10
input3 = [1 1 3 1 2 1 3 3 3 3] 1->4, 3->5, 2->1
output = 4

CONSTRAINTS::
1 <= n <= 100

ALGO::
loop through the array
for each number in array; hashTable[number] = numberOfOccurence
    - if hashTable.get(number); hashTable[number] +=1
    - else hashTable[number] = 1
for number, occurence in hashTable.items()
    - pair += occurence // 2
@return - pair
"if numberOfOccurence is even; then numberOfPair is occurence//2"
"if numberOfOccurence is odd; then pair is occurence//2, odd pair is occurence%2"
"""


def sockMerchant(n, arr):
    """
    :param n: the number of socks in the pile
    :param arr: array[n], the colors of each stock
    :return: the number of pairs.
    """
    if n < 1 or n > 100:
        return None
    hashTable = {}
    for number in arr:
        if hashTable.get(number):
            hashTable[number] += 1
        else:
            hashTable[number] = 1
    numberOfPairs = 0
    for occurence in hashTable.values():
        numberOfPairs += occurence // 2
    return numberOfPairs


print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))  # answer is 2
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))  # answer is 3
print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))  # answer is 4
