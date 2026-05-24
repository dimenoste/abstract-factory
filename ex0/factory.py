from abc import ABC, abstractmethod
from ex0.creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling("My Flameling", "Fire")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("My Pyrodon", "Fire/ Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub("My Aquabub", "Water")

    def create_evolved(self) -> Torragon:
        return Torragon("My Torragon", "Water/ Flying")
