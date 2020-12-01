from abc import ABC, abstractmethod


class Outerwear(ABC):
    @property
    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Outerwear):
    def __init__(self, size):
        self.size = size

    @property
    def get_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Outerwear):
    def __init__(self, height):
        self.height = height

    @property
    def get_consumption(self):
        return 2 * self.height + 0.3


def calculate_total_consumption(items):
    total = 0

    for item in items:
        total += item.get_consumption

    return total


print(calculate_total_consumption([Coat(2), Suit(11), Coat(6)]))
