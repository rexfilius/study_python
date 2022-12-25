"""
Write a function that accepts an array of predicted prices for a particular stock
over the course of time. Calculate the greatest profit that could be made from a
single "buy" transaction followed by a single "sell" transaction.
Assumption - the function will focus on the most profit that
could be made from just one purchase followed by one sale.

input1 = [10, 7, 5, 8, 11, 2, 6]
output1 = buy-5 sell-11 profit-6
"""


def findGreatestProfit(array):
    buyPrice = array[0]
    greatestProfit = 0
    for price in array:
        potentialProfit = price - buyPrice
        if price < buyPrice:
            buyPrice = price
        elif potentialProfit > greatestProfit:
            greatestProfit = potentialProfit
    return greatestProfit


print(findGreatestProfit([10, 7, 5, 8, 11, 2, 6]))
