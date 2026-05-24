from abc import ABC, abstractmethod
from typing import Protocol, TypeGuard

from ex0 import Creature
from ex1 import TransformCapability, HealCapability


class CreatureLike(Protocol):
    def attack(self) -> str: ...

    def describe(self) -> str: ...


class HealCreaturelike(CreatureLike, Protocol):
    def heal(self) -> str: ...


class TransCreatureLike(CreatureLike, Protocol):
    def transform(self) -> str: ...

    def revert(self) -> str: ...


class BattleStrategy[C](ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def act(self, monster: object) -> None:
        pass

    @abstractmethod
    def is_valid(self, monster: object) -> bool:
        pass


class NormalStrategy(BattleStrategy[Creature]):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, monster: object) -> TypeGuard[Creature]:
        return isinstance(monster, Creature)

    def act(self, monster: object) -> None:
        if not self.is_valid(monster):
            raise TypeError("monster should be a Creature type")
        print(monster.attack())


class AggressiveStrategy(BattleStrategy[TransCreatureLike]):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, monster: object) -> TypeGuard[TransCreatureLike]:
        return isinstance(monster, TransformCapability) and isinstance(
            monster, Creature
        )

    def act(self, monster: object) -> None:
        if not self.is_valid(monster):
            raise TypeError(
                "monster should be a TransformCapability and a Creature type"
            )
        print(monster.transform())
        print(monster.attack())
        print(monster.revert())


class DefensiveStrategy(BattleStrategy[HealCreaturelike]):
    def __init__(self) -> None:
        super().__init__()

    def is_valid(self, monster: object) -> TypeGuard[HealCreaturelike]:
        return isinstance(monster, HealCapability) and isinstance(
            monster, Creature
        )

    def act(self, monster: object) -> None:
        if not self.is_valid(monster):
            raise TypeError(
                "monster should be a HealCapability and a Creature type"
            )
        print(monster.attack())
        print(monster.heal())
