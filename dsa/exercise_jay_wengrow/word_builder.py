def wordBuilder(collection):
    """given an array, return a new array containing the combinations of each
    character. [a, b, c, d] => [ab, ac, ad, ba, bc, bd, ca, cb, cd, da, db, dc]
    Time complexity is O(N^2)
    Space complexity is O(N) - because the function creates a new array,
    which will end up holding N^2 strings."""
    nList = []
    for i in range(len(collection)):
        for j in range(len(collection)):
            if i != j:
                nList.append(collection[i] + collection[j])
    return nList


word1 = ['a', 'b', 'c', 'd']
print(wordBuilder(word1))
