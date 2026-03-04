from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    engine.configure_engine(
        FantasyCardFactory(),
        AggressiveStrategy()
    )

    print(engine.get_engine_status())
    print(engine.simulate_turn())


if __name__ == "__main__":
    main()
