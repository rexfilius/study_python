# Shared data can have possibly surprising effects with involving mutable objects
# such as lists and dictionaries. For example, the features list in the code below
# should not be used as a class variable because just a single list would be
# shared by all instances:
class Insect:
    features = []

    def __init__(self, name: str):
        self.name = name

    def add_features(self, features):
        self.features.append(features)


bambi = Insect("House Fly")
tiki = Insect("Mosquito")

bambi.add_features("big eyes")
tiki.add_features("blood sucker")

print(bambi.features)
print()


# Correct design of the class should use an instance variable instead
class BoringInsect:

    def __init__(self, name: str):
        self.name = name
        self.features = []  # creates a new empty list for each insect

    def add_features(self, features):
        self.features.append(features)


ziga = BoringInsect("Ant")
aiko = BoringInsect("Beetle")

ziga.add_features("brown skin")
aiko.add_features("red skin")

print(ziga.features)
print(aiko.features)
