from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def choose_action(self, deck):
        return "Attack aggressively"
