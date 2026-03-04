from typing import Dict
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        return CreatureCard("Dragon", 5, "Epic", 6, 6)

    def create_spell(self, name_or_power=None):
        return SpellCard("Fireball", 3, "Rare", "Damage")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Magic Ring", 2, "Common", 3, "+1 attack")

    def create_themed_deck(self, size: int) -> Dict:
        return {
            "deck_size": size,
            "theme": "Fantasy"
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon"],
            "spells": ["fireball"],
            "artifacts": ["magic_ring"]
        }
