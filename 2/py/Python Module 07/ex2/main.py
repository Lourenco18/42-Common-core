from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    elite = EliteCard(
        "Arcane Warrior",
        6,
        "Epic",
        5,
        8,
        5
    )

    print("Combat phase:")
    print(elite.attack("Enemy"))
    print(elite.defend(3))

    print("\nMagic phase:")
    print(elite.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print(elite.channel_mana(3))


if __name__ == "__main__":
    main()
