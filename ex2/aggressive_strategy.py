from .battle_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capability import TransformCapability


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> None:
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
