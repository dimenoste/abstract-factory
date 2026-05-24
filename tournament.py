from ex0 import Creature
from ex0.factory import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory
from ex1.creature_factory import TransformCreatureFactory
from ex2.strategies import HealCreaturelike, TransCreatureLike
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def create_pair(
    liste_opp: list[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ]
    ],
) -> list[
    tuple[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ],
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ],
    ]
]:

    all_pairs: list[
        tuple[
            tuple[
                CreatureFactory,
                BattleStrategy[
                    Creature | HealCreaturelike | TransCreatureLike
                ],
            ],
            tuple[
                CreatureFactory,
                BattleStrategy[
                    Creature | HealCreaturelike | TransCreatureLike
                ],
            ],
        ]
    ] = [
        (liste_opp[i], liste_opp[j])
        for i in range(len(liste_opp))
        for j in range(i + 1, len(liste_opp))
    ]
    return all_pairs


def battle(
    opponents: list[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ]
    ],
) -> None:
    for pair in create_pair(opponents):
        op1: tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ] = pair[0]
        op2: tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ] = pair[1]
        print("vs.")
        creature1: Creature = op1[0].create_base()
        creature2: Creature = op2[0].create_base()
        strategy1: BattleStrategy[
            Creature | HealCreaturelike | TransCreatureLike
        ] = op1[1]
        strategy2: BattleStrategy[
            Creature | HealCreaturelike | TransCreatureLike
        ] = op2[1]
        print("* Battle *")
        print(creature1.describe())
        print("vs.")
        print(creature2.describe())
        strategy1.act(creature1)
        print("now fight!")
        strategy2.act(creature2)


if __name__ == "__main__":
    print("Testing Factory")
    print("base:")
    my_sprout: HealCreaturelike = HealingCreatureFactory().create_base()
    NormalStrategy().act(my_sprout)

    my_bloom: HealCreaturelike = HealingCreatureFactory().create_evolved()
    DefensiveStrategy().act(my_bloom)

    print()
    print()
    print("Testing Creature with transform capability")
    print("base:")
    my_shiftling: Creature = TransformCreatureFactory().create_base()
    NormalStrategy().act(my_shiftling)

    print("evolved:")
    my_morph: Creature = TransformCreatureFactory().create_evolved()
    AggressiveStrategy().act(my_morph)

    opponents_basic: list[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ]
    ] = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    oppents_tournament1: list[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ]
    ] = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    oppents_tournament2: list[
        tuple[
            CreatureFactory,
            BattleStrategy[Creature | HealCreaturelike | TransCreatureLike],
        ]
    ] = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    battle(opponents_basic)
    print()
    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    try:
        battle(oppents_tournament1)
    except TypeError as e:
        print(f"{e}, invalid creature ")
    print()
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")
    battle(oppents_tournament2)
