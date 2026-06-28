from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capability import TransformCapability


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Battle error, aborting tournament: Invalid Creature "
                f"'{creature.name}' for this aggressive strategy")
        print(creature.transform())  # type:ignore
        print(creature.attack())
        print(creature.revert())  # type:ignore
