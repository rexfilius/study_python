def fib1(n):
    """n = index in the sequence."""
    if n == 0 or n == 1:
        return n
    else:
        return fib1(n - 2) + fib1(n - 1)


def fib2(n, memo=dict()):
    """employs memoization to reduce recursive calls. O(N) time"""
    if n == 0 or n == 1:
        return n
    if not memo.get(n):  # if n not in memo.keys()
        memo[n] = fib2(n - 2, memo) + fib2(n - 1, memo)
    return memo[n]


def fib3(n):
    """Using a bottom-up approach. O(N) time"""
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        temp = a
        a = b
        b = temp + a
    return b


print(fib3(10))
