import ex0.factory as facto


if __name__ == "__main__":
    print("Testing Factory")

    my_flame_base: facto.Creature = facto.FlameFactory().create_base()
    print(my_flame_base.describe())
    print(my_flame_base.attack())

    my_flame_evolved: facto.Creature = facto.FlameFactory().create_evolved()
    print(my_flame_evolved.describe())
    print(my_flame_evolved.attack())

    print()
    print("Testing Factory")
    my_aqua_base: facto.Creature = facto.AquaFactory().create_base()
    print(my_aqua_base.describe())
    print(my_aqua_base.attack())

    my_aqua_evolved: facto.Creature = facto.AquaFactory().create_evolved()
    print(my_aqua_evolved.describe())
    print(my_aqua_evolved.attack())

    print()

    print("Testing battle")
    print(my_flame_base.describe())
    print("vs")
    print(my_aqua_base.describe())
    print(my_flame_base.attack())
    print(my_aqua_base.attack())

