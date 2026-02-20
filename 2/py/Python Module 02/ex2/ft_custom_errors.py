class GardenError(Exception):
    def __init__(self, message="A garden error occurred!"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message="There is a problem with a plant!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="There is a watering problem!"):
        super().__init__(message)


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    """Test PlantError"""
    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)

    """Test WaterError"""
    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_water()
    except GardenError as e:
        print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
