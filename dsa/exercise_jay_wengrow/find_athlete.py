"""
Write a function that accepts two arrays of players and returns an array of
the players who play in both sports. While there are players who share first names
and players who share last names, we can assume there's only one person who has
a particular full name
"""
basketballPlayers = [
    {'firstName': "Jill", 'lastName': "Huang", 'team': "Gators"},
    {'firstName': "Janko", 'lastName': "Barton", 'team': "Sharks"},
    {'firstName': "Wanda", 'lastName': "Vakulskas", 'team': "Sharks"},
    {'firstName': "Jill", 'lastName': "Moloney", 'team': "Gators"},
    {'firstName': "Luuk", 'lastName': "Watkins", 'team': "Gators"}
]
# expected output = ["Jill Huang", "Wanda Vakulskas"]
footballPlayers = [
    {'firstName': "Hanzla", 'lastName': "Radosti", 'team': "32ers"},
    {'firstName': "Tina", 'lastName': "Watkins", 'team': "Barleycorns"},
    {'firstName': "Alex", 'lastName': "Patel", 'team': "32ers"},
    {'firstName': "Jill", 'lastName': "Huang", 'team': "Barleycorns"},
    {'firstName': "Wanda", 'lastName': "Vakulskas", 'team': "Barleycorns"}
]


def findCommonAthlete(array1, array2):
    """Nested Loops. O(N*M) time"""
    newArray = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i]['firstName'] == array2[j]['firstName'] and \
                    array1[i]['lastName'] == array2[j]['lastName']:
                newArray.append(array1[i]['firstName'] + ' ' + array1[i]['lastName'])
                break
    return newArray


def findCommonAthlete_2(array1, array2):
    """O(N+M) Time. Better than previous function"""
    newArray = []
    hashTable = {}
    for i in range(len(array1)):
        hashTable[array1[i]['firstName'] + array1[i]['lastName']] = True
    for j in range(len(array2)):
        if hashTable.get(array2[j]['firstName'] + array2[j]['lastName']):
            newArray.append(array2[j]['firstName'] + ' ' + array2[j]['lastName'])
    return newArray


print(findCommonAthlete(basketballPlayers, footballPlayers))
print(findCommonAthlete_2(basketballPlayers, footballPlayers))
