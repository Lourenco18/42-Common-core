from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ..ex1.SpellCard import SpellCard


class FantasyCardFactory(CardFactory):

    def create_creature(self):
        return CreatureCard("Dragon", 5, "Epic", 6, 6)

    def create_spell(self):
        return SpellCard("Fireball", 3, "Rare", "Deal 5 damage")
