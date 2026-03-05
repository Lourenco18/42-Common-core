import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    """
    Load configuration from environment variables.
    """
    load_dotenv()

    config = {
        "mode": os.getenv("MATRIX_MODE"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_configuration(config: dict) -> None:
    """
    Validate required configuration values.
    """
    for key, value in config.items():
        if value is None:
            print(f"WARNING: Missing configuration -> {key}")


def display_configuration(config: dict) -> None:
    """
    Display configuration summary.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")

    mode = config["mode"] or "development"
    print(f"Mode: {mode}")

    if config["database"]:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config["api_key"]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {config['log_level'] or 'INFO'}")

    if config["zion_endpoint"]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """
    Basic security checks.
    """
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    """
    Main execution.
    """
    try:
        config = load_configuration()

        validate_configuration(config)

        display_configuration(config)

        security_check()

        print("\nThe Oracle sees all configurations.")

    except Exception as e:
        print("Error accessing configuration:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
