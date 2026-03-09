"""Configuration file parser for A-Maze-ing."""

import sys
from dataclasses import dataclass
from typing import Optional


REQUIRED_KEYS: list[str] = [
    "WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT",
]


@dataclass
class MazeConfig:
    """Parsed maze configuration.

    Attributes:
        width: Number of cells horizontally.
        height: Number of cells vertically.
        entry: (x, y) entry coordinates.
        exit_: (x, y) exit coordinates.
        output_file: Path to write the output maze.
        perfect: Whether to generate a perfect maze.
        seed: Optional random seed.
        algorithm: Generation algorithm name (default 'dfs').
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit_: tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None
    algorithm: str = "dfs"


def parse_config(path: str) -> MazeConfig:
    """Parse a KEY=VALUE configuration file.

    Args:
        path: Path to the configuration file.

    Returns:
        A MazeConfig dataclass with validated values.

    Raises:
        SystemExit: On any configuration error.
    """
    raw: dict[str, str] = {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    _error(
                        f"Line {lineno}: invalid format '{line}' "
                        "(expected KEY=VALUE)"
                    )
                key, _, value = line.partition("=")
                raw[key.strip().upper()] = value.strip()
    except FileNotFoundError:
        _error(f"Configuration file not found: '{path}'")
    except OSError as exc:
        _error(f"Cannot read configuration file: {exc}")

    for key in REQUIRED_KEYS:
        if key not in raw:
            _error(f"Missing mandatory key '{key}' in config file.")

    width = _parse_int(raw["WIDTH"], "WIDTH", min_val=2)
    height = _parse_int(raw["HEIGHT"], "HEIGHT", min_val=2)
    entry = _parse_coords(raw["ENTRY"], "ENTRY", width, height)
    exit_ = _parse_coords(raw["EXIT"], "EXIT", width, height)

    if entry == exit_:
        _error("ENTRY and EXIT must be different cells.")

    output_file = raw["OUTPUT_FILE"]
    if not output_file:
        _error("OUTPUT_FILE cannot be empty.")

    perfect_str = raw["PERFECT"].lower()
    if perfect_str not in ("true", "false", "1", "0"):
        _error(f"PERFECT must be True or False, got '{raw['PERFECT']}'.")
    perfect = perfect_str in ("true", "1")

    seed: Optional[int] = None
    if "SEED" in raw:
        seed = _parse_int(raw["SEED"], "SEED")

    algorithm = raw.get("ALGORITHM", "dfs").lower()
    if algorithm not in ("dfs",):
        print(
            f"Warning: unknown algorithm '{algorithm}', using 'dfs'.",
            file=sys.stderr,
        )
        algorithm = "dfs"

    return MazeConfig(
        width=width,
        height=height,
        entry=entry,
        exit_=exit_,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
        algorithm=algorithm,
    )


def _error(msg: str) -> None:
    """Print error and exit."""
    print(f"[ERROR] {msg}", file=sys.stderr)
    sys.exit(1)


def _parse_int(value: str, key: str, min_val: Optional[int] = None) -> int:
    """Parse a string as a positive integer."""
    try:
        result = int(value)
    except ValueError:
        _error(f"'{key}' must be an integer, got '{value}'.")
        return 0  # unreachable but satisfies mypy
    if min_val is not None and result < min_val:
        _error(f"'{key}' must be >= {min_val}, got {result}.")
    return result


def _parse_coords(
    value: str, key: str, width: int, height: int
) -> tuple[int, int]:
    """Parse 'x,y' coordinates and validate bounds."""
    parts = value.split(",")
    if len(parts) != 2:
        _error(f"'{key}' must be in format 'x,y', got '{value}'.")
    x = _parse_int(parts[0].strip(), f"{key}.x", min_val=0)
    y = _parse_int(parts[1].strip(), f"{key}.y", min_val=0)
    if x >= width:
        _error(f"'{key}' x={x} is out of bounds (WIDTH={width}).")
    if y >= height:
        _error(f"'{key}' y={y} is out of bounds (HEIGHT={height}).")
    return (x, y)
