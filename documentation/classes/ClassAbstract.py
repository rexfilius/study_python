from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):

    def process(self):
        print("a laptop is running")


# computer = Computer()  # error
# computer.process()   # error

laptop = Laptop()
laptop.process()