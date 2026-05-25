from ex1 import HealingCreatureFactory as healfacto
from ex1.creature_factory import TransformCreatureFactory as trans


if __name__ == "__main__":
    print("Testing Factory")
    print("Testing Creature with healing capability")
    print("base:")
    my_sprout = healfacto().create_base()

    print(my_sprout.describe())
    print(my_sprout.attack())
    print(my_sprout.heal())
    print()
    print("evolved:")
    my_bloom = healfacto().create_evolved()
    print(my_bloom.describe())
    print(my_bloom.attack())
    print(my_bloom.heal())

    print()
    print()
    print("Testing Creature with transform capability")
    print("base:")
    my_shiftling = trans().create_base()
    print(my_shiftling.describe())
    print(my_shiftling.attack())
    print(my_shiftling.transform())
    print(my_shiftling.attack())
    print(my_shiftling.revert())
    print()
    print("evolved:")
    my_morph = trans().create_evolved()
    print(my_morph.describe())
    print(my_morph.attack())
    print(my_morph.transform())
    print(my_morph.attack())
    print(my_morph.revert())
