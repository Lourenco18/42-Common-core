import sys
import importlib


def check_package(package_name: str) -> tuple[bool, str]:
    """
    Check if a package is installed and return its version.
    """
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "Unknown")
        return True, version
    except ImportError:
        return False, ""


def show_dependency_status() -> bool:
    """
    Check required dependencies and display status.
    """
    packages = ["pandas", "numpy", "matplotlib", "requests"]

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok = True

    for pkg in packages:
        installed, version = check_package(pkg)

        if installed:
            print(f"[OK] {pkg} ({version}) - Ready")
        else:
            print(f"[MISSING] {pkg} - Not installed")
            all_ok = False

    return all_ok


def run_analysis() -> None:
    """
    Perform sample matrix data analysis.
    """
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")

        data = np.random.normal(50, 15, 1000)

        df = pd.DataFrame({"matrix_signal": data})

        print(f"Processing {len(df)} data points...")

        plt.figure()
        df["matrix_signal"].hist(bins=30)

        plt.title("Matrix Signal Distribution")
        plt.xlabel("Signal Strength")
        plt.ylabel("Frequency")

        plt.savefig("matrix_analysis.png")

        print("\nGenerating visualization...")
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except Exception as e:
        print("Error during analysis:", e)


def main() -> None:
    """
    Main execution.
    """
    deps_ok = show_dependency_status()

    if not deps_ok:
        print("\nSome dependencies are missing.")
        print("Install using pip:")
        print("pip install -r requirements.txt")
        print("\nOr using Poetry:")
        print("poetry install")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
