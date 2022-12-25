def isOpeningBrace(character):
    return character in ['(', '[', '{']


def isClosingBrace(character):
    return character in [')', ']', '}']


def isAMatch(openBrace, closeBrace):
    matches = {'(': ')', '[': ']', '{': '}'}
    return matches[openBrace] == closeBrace


def hasValidBraces(string):
    nList = []
    for character in string:
        if isOpeningBrace(character):
            nList.append(character)
        if isClosingBrace(character):
            if len(nList) == 0:
                return False
            else:
                openBrace = nList.pop()
                if isAMatch(openBrace, character):
                    continue
                else:
                    return False
    return len(nList) == 0


str1 = "())"  # invalid - False
str2 = ")()"  # invalid - False
str3 = "()"  # valid - True
str4 = "()[]{}"  # valid - True
str5 = "(]"  # invalid - False
str6 = "([}]"  # invalid - False
str7 = "{[]}"  # valid - True
print(hasValidBraces(''))
