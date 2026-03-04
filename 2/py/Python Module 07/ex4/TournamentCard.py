from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: Dict) -> Dict:
        return {"card_played": self.name}

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> Dict:
        return {"defended": True}

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_power}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> Dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def get_tournament_stats(self) -> Dict:
        return self.get_rank_info()
