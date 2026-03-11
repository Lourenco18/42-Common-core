from TournamentCard import TournamentCard
from TournamentPlatform import TournamentPlatform


def main():

    platform = TournamentPlatform()

    c1 = TournamentCard("Dragon", 5, "Epic", 6, 6, 90)
    c2 = TournamentCard("Goblin", 2, "Common", 2, 2, 40)
    c3 = TournamentCard("Phoenix", 7, "Legendary", 8, 5, 95)

    platform.register_card(c1)
    platform.register_card(c2)
    platform.register_card(c3)

    top_cards = platform.get_top_cards()

    for card in top_cards:
        print(card.name, card.get_rank())


if __name__ == "__main__":
    main()
