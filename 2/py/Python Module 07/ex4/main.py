from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Dragon", 5, "Epic", 6, 6)
    wizard = TournamentCard("Wizard", 4, "Rare", 5, 5)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print(platform.create_match(id1, id2))
    print(platform.generate_tournament_report())


if __name__ == "__main__":
    main()
