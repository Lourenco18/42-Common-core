class TournamentPlatform:

    def __init__(self):
        self.cards = []

    def register_card(self, card):
        self.cards.append(card)

    def get_top_cards(self):

        return sorted(
            self.cards,
            key=lambda c: c.get_rank(),
            reverse=True
        )
