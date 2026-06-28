from ex1 import HealingCreatureFactory, TransformCreatureFactory


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()

    print("base:")
    sproutling = heal_factory.create_base()
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print("evolved:")
    bloomelle = heal_factory.create_evolved()
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print()

    print("Testing Creature with transform capability")
    trans_factory = TransformCreatureFactory()

    print("base:")
    shiftling = trans_factory.create_base()
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print("evolved:")
    morphagon = trans_factory.create_evolved()
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())
