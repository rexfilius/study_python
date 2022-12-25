class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        grade = sum(self.scores) // len(self.scores)
        if 90 <= grade <= 100:
            return 'O'
        elif 80 <= grade < 90:
            return 'E'
        elif 70 <= grade < 80:
            return 'A'
        elif 55 <= grade < 70:
            return 'P'
        elif 40 <= grade < 55:
            return 'D'
        elif grade < 40:
            return 'T'


# INPUT
# Heraldo Memelli 8135627
# 2
# 100 80
# OUTPUT
# Name: Memelli, Heraldo
# ID: 8135627
# Grade: O

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
