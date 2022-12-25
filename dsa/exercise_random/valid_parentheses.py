def validParentheses(string):
    nList = []
    for character in string:
        if character == '(':
            nList.append(character)
        if character == ')':
            if len(nList) == 0:
                return False
            else:
                nList.pop()
    return len(nList) == 0


str1 = "())"  # invalid - False
str2 = "()"  # valid - True
str3 = "()[]{}"  # valid - True
str4 = "(])"  # invalid - True
str5 = ")([}]"  # invalid - False
print(validParentheses(str5))
