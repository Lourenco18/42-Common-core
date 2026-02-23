# ft_custom_errors.py

class GardenError(Exception):
    """A basic error for garden problems"""
    pass


class PlantError(GardenError):
    """For problems with plants"""
    pass


class WaterError(GardenError):
    """For problems with watering"""
    pass


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)
    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)
    print("Testing catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_water()
    except GardenError as e:
        print("Caught a garden error:", e)
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
