from AggressiveStrategy import AggressiveStrategy
from FantasyCardFactory import FantasyCardFactory
from GameEngine import GameEngine


def main():

    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()

    engine = GameEngine(strategy, factory)

    result = engine.start()

    print(result)


if __name__ == "__main__":
    main()
