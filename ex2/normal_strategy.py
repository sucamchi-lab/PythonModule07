from .battle_strategy import BattleStrategy
from ex0.creature import Creature


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, Creature):
            return True
        return False

    def act(self, creature: Creature) -> None:
        print(creature.attack())
