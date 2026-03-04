from typing import Dict, List
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = f"{card.name.lower()}_{len(self.cards)+1}"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        winner = card1 if card1.attack_power >= card2.attack_power else card2
        loser = card2 if winner == card1 else card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List:
        return sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )

    def generate_tournament_report(self) -> Dict:
        avg_rating = (
            sum(card.rating for card in self.cards.values()) /
            len(self.cards)
        )

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating
        }
