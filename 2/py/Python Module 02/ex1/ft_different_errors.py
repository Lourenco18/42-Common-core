def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden = {"rose": 5, "tulip": 10}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    garden_operations()

    print("Testing multiple errors together...")
    try:
        int("xyz")
        5 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
