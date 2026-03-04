from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "effect": "Elite unit deployed"
        }

    # Combatable methods

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        damage_taken = min(incoming_damage, self.health)
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # Magical methods

    def cast_spell(self, spell_name: str, targets: List[str]) -> Dict:
        mana_used = 2
        self.mana -= mana_used

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana": self.mana
        }
