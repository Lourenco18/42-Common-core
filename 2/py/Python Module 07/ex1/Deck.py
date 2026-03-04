import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:
        total = len(self.cards)
        avg_cost = (sum(card.cost for card in self.cards) / total if total else 0)

        return {
            "total_cards": total,
            "avg_cost": avg_cost
        }
