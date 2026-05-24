from ex0.factory import CreatureFactory
from ex1.concrete_creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("My Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("My Bloomelle", "Grass/Fairy")


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Normal/Dragon", "Grass/Fairy")
