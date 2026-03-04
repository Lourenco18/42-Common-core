from typing import Dict, List
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        damage = len(hand) * 2
        return {
            "strategy": "Aggressive",
            "cards_played": len(hand),
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return available_targets
