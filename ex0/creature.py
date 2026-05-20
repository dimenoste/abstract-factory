from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_creature: str) -> None:
        self.name: str = name
        self.type_creature: str = type_creature

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return ''


class Flameling(Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} uses Ember!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                f"{self.type_creature} type Creature!")


class Pyrodon(Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} uses Flamethrower!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                f"{self.type_creature} type Creature!")


class Aquabub(Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} uses Water Gun!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                f"{self.type_creature} type Creature!")


class Torragon(Creature):
    def __init__(self, name: str, type_creature: str) -> None:
        super().__init__(name, type_creature)

    def attack(self) -> str:
        return (f"{type(self).__name__} uses Hydro Pump!")

    def describe(self) -> str:
        return (f"{type(self).__name__} is a "
                f"{self.type_creature} type Creature!")
