from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self, other):
        pass

    def describe(self):
        return f"{self.name} is a {self.type} type Creature."
