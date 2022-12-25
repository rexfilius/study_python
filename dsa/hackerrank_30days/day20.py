if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    numSwaps = 0
    for i in range(0, n - 1):
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                numSwaps += 1

    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
