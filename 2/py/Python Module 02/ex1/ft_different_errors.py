

def garden_operations():
    print("Testing ValueError...")
    try:
        raise ValueError("invalid literal for int()")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        raise ZeroDivisionError("division by zero")
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
        raise KeyError("'missing_plant'")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("Testing multiple errors together...")
    try:

        raise ValueError("simulated multiple errors")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
