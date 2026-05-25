from ex1 import HealCapability, TransformCapability
from ex0 import Creature


class Sproutling(HealCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return f"{type(self).__name__} uses Vine Whip!"

    def describe(self) -> str:
        return (
            f"{type(self).__name__} is a {self.type_creature} type Creature!"
        )

    def heal(self) -> str:
        return f"{type(self).__name__} heals itself for a small amount"


class Bloomelle(HealCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return f"{type(self).__name__}  uses Petal Dance!"

    def describe(self) -> str:
        return (
            f"{type(self).__name__} is a {self.type_creature}  type Creature!"
        )

    def heal(self) -> str:
        return f"{type(self).__name__} heals itself for a large amount"


class Shiftling(TransformCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        TransformCapability.__init__(self)
        Creature.__init__(self, name=name, type_creature=type_creature)

    def attack(self) -> str:
        attack_type: str = "attacks normally"
        if self.transformed:
            attack_type = "performs a boosted strike!"
        return f"{type(self).__name__} {attack_type}"

    def describe(self) -> str:
        return (
            f"{type(self).__name__} is a {self.type_creature} type Creature!"
        )

    def transform(self) -> str:
        self.transformed = True
        return f"{type(self).__name__} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{type(self).__name__} returns to normal."


class Morphagon(TransformCapability, Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        TransformCapability.__init__(self)
        Creature.__init__(self, name=name, type_creature=type_creature)

    def attack(self) -> str:
        attack_type: str = "attacks normally"
        if self.transformed:
            attack_type = "unleashes a devastating morph strike!"
        return f"{type(self).__name__} {attack_type}"

    def describe(self) -> str:
        return (
            f"{type(self).__name__} is a {self.type_creature}  type Creature!"
        )

    def transform(self) -> str:
        self.transformed = True
        return f"{type(self).__name__} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{type(self).__name__} stabilizes its form."
