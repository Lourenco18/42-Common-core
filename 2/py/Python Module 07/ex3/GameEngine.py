class GameEngine:

    def __init__(self, strategy, factory):
        self.strategy = strategy
        self.factory = factory

    def start(self):
        creature = self.factory.create_creature()
        spell = self.factory.create_spell()

        action = self.strategy.choose_action(None)

        return {
            "creature": creature.name,
            "spell": spell.name,
            "strategy": action
        }
