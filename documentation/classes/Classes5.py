# Generally speaking, instance variables are for data unique to each instance and
# class variables are for attributes and methods shared by all instances of the class
class Bird:
    kind = "flightless"  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


joey = Bird("Joey")
ada = Bird("Ada")

print(joey.kind)
print(ada.kind)
print()

print(joey.name)
print(ada.name)
