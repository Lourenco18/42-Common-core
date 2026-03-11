from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int):
        super().__init__(name, cost, rarity)
        self.durability = durability

    def play(self, game_state: dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Artifact placed on battlefield"
        }
