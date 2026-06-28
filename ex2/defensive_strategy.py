from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capability import HealCapability


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this defensive strategy.")
        print(creature.attack())
        print(creature.heal())  # type:ignore
