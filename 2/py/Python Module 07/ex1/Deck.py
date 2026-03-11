import random
from typing import List
from ex0.Card import Card


class Deck:

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def deck_size(self):
        return len(self.cards)
