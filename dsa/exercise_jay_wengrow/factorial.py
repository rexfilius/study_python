def factorialRecurse(number):
    if number == 1:
        return 1
    else:
        return number * factorialRecurse(number - 1)


def factorial(number):
    product = 1
    for n in range(1, number + 1):
        product *= n
    return product


print(factorialRecurse(5))
print(factorial(5))
