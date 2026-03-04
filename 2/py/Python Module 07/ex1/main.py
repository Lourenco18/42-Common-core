from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "Damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2,
                               "Common", 3, "+1 mana per turn"))

    print(deck.get_deck_stats())

    deck.shuffle()

    while deck.cards:
        card = deck.draw_card()
        print(card.play({}))


if __name__ == "__main__":
    main()
