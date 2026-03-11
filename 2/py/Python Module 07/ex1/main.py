from Deck import Deck
from SpellCard import SpellCard
from ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main():

    deck = Deck()

    c1 = CreatureCard("Dragon", 5, "Epic", 6, 6)
    s1 = SpellCard("Fireball", 3, "Rare", "Deal 5 damage")
    a1 = ArtifactCard("Magic Sword", 4, "Common", 10)

    deck.add_card(c1)
    deck.add_card(s1)
    deck.add_card(a1)

    print("Deck size:", deck.deck_size())

    deck.shuffle()

    print("Draw card:", deck.draw_card().name)
    print("Deck size:", deck.deck_size())


if __name__ == "__main__":
    main()
