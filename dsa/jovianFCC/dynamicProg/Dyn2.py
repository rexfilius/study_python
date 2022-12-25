"""
KNAPSACK PROBLEM
You are in charge of selecting a football team from a large pool of players. Each
player has a cost, and a rating. You have a limited budget. What is the highest
total rating of a team that fits within your budget. Assume that there's no
minimum or maximum team size.

restated - Given n elements, each of which has a weight and a profit, determine the
maximum profit that can be obtained by selecting a subset of the elements weighing
no more than w.
profit = [2, 3, 1, 5, 4, 7]  chosen = 3, 5, 4, 7
weight = [4, 5, 1, 3, 2, 5]  chosen = 5, 3, 2, 5 = 15
capacity = 15 (max weight allowed)
"""


def maxProfitRecursive(weights, profits, capacity, index=0):
    if index == len(weights):
        return 0
    elif weights[index] > capacity:
        return maxProfitRecursive(weights, profits, capacity, index + 1)
    else:
        option1 = maxProfitRecursive(weights, profits, capacity, index + 1)
        option2 = profits[index] + maxProfitRecursive(
            weights, profits, capacity - weights[index], index + 1)
        return max(option1, option2)


def maxProfitDynamic(weights, profits, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i + 1][c] = table[i][c]
            else:
                table[i + 1][c] = max(
                    table[i][c], profits[i] + table[i][c - weights[i]])
    return table[-1][-1]
