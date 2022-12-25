def isOpeningBrace(character):
    return character in ['(', '[', '{']


def isClosingBrace(character):
    return character in [')', ']', '}']


def isAMatch(openBrace, closeBrace):
    matches = {'(': ')', '[': ']', '{': '}'}
    return matches[openBrace] == closeBrace


def hasValidBraces(string):
    """Does not work well for a large length"""
    nList = []
    for character in string:
        if isOpeningBrace(character):
            nList.append(character)
        if isClosingBrace(character):
            if len(nList) == 0:
                return 'NO'  # False
            else:
                openBrace = nList.pop()
                if isAMatch(openBrace, character):
                    continue
                else:
                    return 'NO'  # False
    return 'YES'  # len(nList) == 0


def hasValidBraces2(string):
    """Works well for a large length"""
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '').replace('[]', '').replace('{}', '')
    if len(string) > 0:
        return 'NO'
    else:
        return 'YES'


str1 = "())"  # invalid - False
str2 = ")()"  # invalid - False
str3 = "()"  # valid - True
str4 = "()[]{}"  # valid - True
str5 = "(]"  # invalid - False
str6 = "([}]"  # invalid - False
str7 = "{[]}"  # valid - True
print(hasValidBraces(''))
