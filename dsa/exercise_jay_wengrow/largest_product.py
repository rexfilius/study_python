def largestProduct(array):
    largestSoFar = array[0] * array[1] * array[2]
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            while k < len(array):
                if array[i] * array[j] * array[k] > largestSoFar:
                    largestSoFar = array[i] * array[j] * array[k]
                k += 1
            j += 1
        i += 1
