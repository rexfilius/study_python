from algoFreeCodeCamp.courseJovian.dynamicProg.Dyn2 \
    import maxProfitRecursive, maxProfitDynamic

weights1 = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profits1 = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
capacity1 = 165  # output = 309

weights2 = [4, 5, 6]
profits2 = [1, 2, 3]
capacity2 = 3  # output = 0

weights3 = [4, 5, 1]
profits3 = [1, 2, 3]
capacity3 = 4  # output = 3

weights4 = [41, 50, 49, 59, 55, 57, 60]
profits4 = [442, 525, 511, 593, 546, 564, 617]
capacity4 = 170  # output = 1735

weights5 = [4, 5, 6]
profits5 = [1, 2, 3]
capacity5 = 15  # output = 6

weights6 = [4, 5, 1, 3, 2, 5]
profits6 = [2, 3, 1, 5, 4, 7]
capacity6 = 15  # output = 19

print(maxProfitRecursive(weights1, profits1, capacity1))
print(maxProfitRecursive(weights2, profits2, capacity2))
print(maxProfitRecursive(weights3, profits3, capacity3))
print(maxProfitRecursive(weights4, profits4, capacity4))
print(maxProfitRecursive(weights5, profits5, capacity5))
print(maxProfitRecursive(weights6, profits6, capacity6))
print()

print(maxProfitDynamic(weights1, profits1, capacity1))
print(maxProfitDynamic(weights2, profits2, capacity2))
print(maxProfitDynamic(weights3, profits3, capacity3))
print(maxProfitDynamic(weights4, profits4, capacity4))
print(maxProfitDynamic(weights5, profits5, capacity5))
print(maxProfitDynamic(weights6, profits6, capacity6))
