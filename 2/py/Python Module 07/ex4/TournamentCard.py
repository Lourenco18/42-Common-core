from ex0.CreatureCard import CreatureCard
from .Rankable import Rankable


class TournamentCard(CreatureCard, Rankable):

    def __init__(self, name, cost, rarity, attack, health, rank):
        super().__init__(name, cost, rarity, attack, health)
        self.rank = rank

    def get_rank(self):
        return self.rank
