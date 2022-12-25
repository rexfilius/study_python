def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print('Enter a non-negative integer: ')
number = int(input())
print(f"Factorial of {number} = {factorial(number)}")
