from EliteCard import EliteCard


def main():

    elite = EliteCard("Archmage Dragon", 6, "Legendary", 8, 8)

    print(elite.attack("Enemy Knight"))

    print(elite.cast_spell())


if __name__ == "__main__":
    main()
