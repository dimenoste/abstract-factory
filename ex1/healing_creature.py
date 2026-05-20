from ex1 import HealCapability, TransformCapability
from ex0 import Creature




class Sproutling(HealCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} Vine Whip!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                "Grass type Creature!")

    def heal(self) -> str:
        return (f"{type(self).__name__} heals"
                "itself for a small amount")


class Bloomelle(HealCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} Vine Whip!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                "Grass/Fairy type Creature!")

    def heal():
        return (f"{type(self).__name__} heals"
                "itself for a large amount")
