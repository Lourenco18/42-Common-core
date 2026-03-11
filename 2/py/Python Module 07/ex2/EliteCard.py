from ex0.CreatureCard import CreatureCard
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(CreatureCard, Combatable, Magical):

    def attack(self, target):
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack
        }

    def cast_spell(self):
        return {
            "caster": self.name,
            "spell": "Elite Magic Blast"
        }
