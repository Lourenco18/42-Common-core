from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    dragon = CreatureCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5
    )

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlayable with 6 mana?")
    print(dragon.is_playable(6))
    print(dragon.play({}))

    print("\nAttack test:")
    print(dragon.attack_target("Goblin Warrior"))

    print("\nPlayable with 3 mana?")
    print(dragon.is_playable(3))


if __name__ == "__main__":
    main()
