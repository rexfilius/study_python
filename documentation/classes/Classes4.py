class Droid:
    kind = ""

    def __init__(self, name: str, planet: str):
        self.name = name
        self.planet = planet

    def print_droid_details(self):
        print(f"Droid's name: {self.name}, planet: {self.planet}, kind: {self.kind}")


# Usually, a method is called right after it is bound
mad_droid = Droid("Hepha", "Sorza")
mad_droid.print_droid_details()

# However, it is not necessary to call a method right away:
# "mad_droid.print_droid_details" is a method object, and can be stored away and
# called at a later time
x_droid = mad_droid.print_droid_details
print(x_droid())

mad_droid.kind = "Melancholy"
mad_droid.print_droid_details()
