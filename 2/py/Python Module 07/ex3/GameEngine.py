from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory = None
        self.strategy = None

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        hand = [
            self.factory.create_creature(),
            self.factory.create_spell()
        ]
        return self.strategy.execute_turn(hand, [])

    def get_engine_status(self) -> Dict:
        return {
            "factory": type(self.factory).__name__,
            "strategy": self.strategy.get_strategy_name()
        }
