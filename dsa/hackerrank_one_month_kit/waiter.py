"""

"""
from math import sqrt


def getQprimes(q):
    n, count, out = 2, 0, []
    while count < q:
        isPrime = True
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            out.append(n)
            count += 1
        n += 1
    return out


def waiter(number, q):
    primes, answer = getQprimes(q), []
    for i in primes:
        B = []
        A = []
        for j in reversed(number):
            if j % i == 0:
                B.append(j)
            else:
                A.append(j)
        number = A
        answer += reversed(B)

    answer += reversed(A)
    return answer


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
