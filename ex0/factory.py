from abc import ABC, abstractmethod
from ex0 import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Flameling("My Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("My Pyrodon", "Fire/ Flying")


class AquaFactory():
    def create_base(self) -> Creature:
        return Aquabub("My Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("My Torragon", "Water/ Flying")
