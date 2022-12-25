"""
Julius Caesar protected his confidential information by encrypting it using a
cipher. Caesar's cipher shifts each letter by a number of letters. If the shift
takes you past the end of the alphabet, just rotate back to the front of the
alphabet. In the case of a rotation by 3; w, x, y and z would map to z, a, b and c.
Note: The cipher only encrypts letters; symbols, such as '-', remain unencrypted.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

CONSTRAINTS::
0 <= k <= 100
s is a valid ASCII string without any spaces.

EXAMPLE::
s = middle-Outz = length is 11
k = 2
output = okffng-Qwvb

s = Always-Look-on-the-Bright-Side-of-Life = length is 38
k = 5
output = Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj

ALGO::
alphabet:      abcdefghijklmnopqrstuvwxyz
indices:       0 ... 25
parameters - k, number of letter to rotate the alphabet by
           - string, the unecrypted string
variables - encryptedString, hashTable
for char in alphabet:
    - hashTable[char] = alphabet.index(char)
for index, letter in enumerate(string):
    - if letter == '-', encrptedString += letter, continue
    - get index of letter in alphabet,
        - indexInAlphabet = hashTable[letter]
        - if indexInAlphabet + k is less than or equal to 25
            - rotatedLetter = alphabet[index+k]
            - encryptedString += rotatedLetter
        - else
            - x = indexInAlphabet minus 25
            - rotatedLetter = alphabet[x+k]
            - encryptedString += rotatedLetter
@return encryptedString
"""


def caesarCipher(s, k):
    """
    This solution ignores casing.
    :param s: the unecrypted string
    :param k: the number of letters to rotate the alphabet by
    :return: enStr: the encrypted String.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetLength = len(alphabet)
    hashTable = {}
    encryptedString = ''

    for char in alphabet:
        hashTable[char] = alphabet.index(char)
    for letter in s.casefold():
        if not letter.isalpha():
            encryptedString += letter
            continue
        indexInAlphabet = hashTable[letter]
        if indexInAlphabet + k <= alphabetLength - 1:
            encryptedString += alphabet[indexInAlphabet + k]
        else:
            x = indexInAlphabet - alphabetLength
            encryptedString += alphabet[x + k]
    return encryptedString


def caesarCipher_2(s: str, k: int):
    """This solution considers casing."""
    string = list(s)
    length = len(s)
    # when loop gets to a character that is not a letter,
    # it just continues to next Index
    for i in range(length):
        # ord-Z is 90 and ord-A is 65
        if ord("Z") >= ord(string[i]) >= ord("A"):
            asciiCode = ord(s[i]) + k
            while asciiCode > ord("Z"):
                asciiCode = asciiCode - ord("Z") + ord("A") - 1
            string[i] = chr(asciiCode)
        # ord-z is 122 and ord-a is 97
        elif ord("z") >= ord(string[i]) >= ord("a"):
            asciiCode = ord(s[i]) + k
            while asciiCode > ord("z"):
                asciiCode = asciiCode - ord("z") + ord("a") - 1
            string[i] = chr(asciiCode)
    return "".join(string)


print(caesarCipher('middle-Outz', 2))
# okffng-Qwvb

print(caesarCipher_2('Always-Look-on-the-Bright-Side-of-Life', 5))
# Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj

print(ord('a'))
