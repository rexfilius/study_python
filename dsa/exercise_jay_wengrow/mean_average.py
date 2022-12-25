def averageOfEvenNumbers(collection):
    """
    accepts an array of numbers and returns the mean average of all its even numbers.
    The mean average of even numbers will be defined as the sum of the even numbers
    divided by the count of even numbers, so we keep track of both the sum
    and the count.
    Time complexity is O(N).
    """
    sumOfNumbers = 0.0
    countOfEvenNumbers = 0
    for element in collection:
        if element % 2 == 0:
            sumOfNumbers += element
            countOfEvenNumbers += 1
    return sumOfNumbers / countOfEvenNumbers


array1 = [3, 2, 4, 5, 7, 9, 6]
print(averageOfEvenNumbers(array1))
