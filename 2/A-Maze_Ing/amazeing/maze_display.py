"""Terminal ASCII rendering and interactive menu for A-Maze-ing."""

import os
import sys
from typing import Optional
from mazegen_pkg.mazegen.generator import (
    MazeGenerator,
    NORTH, EAST, SOUTH, WEST,
)

# ANSI colour codes
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"

COLOUR_SETS: list[dict[str, str]] = [
    {   # Default: white walls
        "wall": "\033[37m",
        "path": "\033[36m",
        "entry": "\033[35m",
        "exit": "\033[31m",
        "cell": "\033[40m",
        "fortytwo": "\033[90m",
    },
    {   # Yellow walls
        "wall": "\033[33m",
        "path": "\033[36m",
        "entry": "\033[35m",
        "exit": "\033[31m",
        "cell": "\033[40m",
        "fortytwo": "\033[32m",
    },
    {   # Green walls
        "wall": "\033[32m",
        "path": "\033[36m",
        "entry": "\033[35m",
        "exit": "\033[31m",
        "cell": "\033[40m",
        "fortytwo": "\033[34m",
    },
]


def _clear() -> None:
    """Clear terminal screen."""
    os.system("clear" if os.name == "posix" else "cls")


def _path_coords(
    gen: MazeGenerator, solution: str
) -> set[tuple[int, int]]:
    """Convert solution direction string to set of (x,y) coordinates."""
    from mazegen_pkg.mazegen.generator import DIRECTION_DELTA
    coords: set[tuple[int, int]] = set()
    x, y = gen.entry
    coords.add((x, y))
    for ch in solution:
        d_map = {"N": NORTH, "E": EAST, "S": SOUTH, "W": WEST}
        d = d_map.get(ch)
        if d is None:
            continue
        dx, dy = DIRECTION_DELTA[d]
        x += dx
        y += dy
        coords.add((x, y))
    return coords


def render_maze(
    gen: MazeGenerator,
    show_path: bool = False,
    colour_idx: int = 0,
) -> None:
    """Render the maze to terminal using ASCII block characters.

    Args:
        gen: Generated MazeGenerator instance.
        show_path: Whether to highlight the solution path.
        colour_idx: Index into COLOUR_SETS.
    """
    colours = COLOUR_SETS[colour_idx % len(COLOUR_SETS)]
    solution = gen.get_solution() if show_path else ""
    path_set: set[tuple[int, int]] = (
        _path_coords(gen, solution) if show_path else set()
    )
    ft_set: set[tuple[int, int]] = set(gen.forty_two_cells)
    ex, ey = gen.entry
    xx, xy = gen.exit_
    w = gen.width
    h = gen.height

    # Each cell is rendered as 2 cols x 1 row of chars.
    # We build a (2h+1) x (2w+1) char grid.
    # Use block characters for walls: '█' for wall, ' ' for open.
    WALL_CH = "█"
    OPEN_CH = " "
    PATH_CH = "·"

    lines: list[str] = []
    for y in range(h):
        # Top border of row y
        top = ""
        for x in range(w):
            cell = gen.cells[y][x]
            top += WALL_CH  # corner
            top += WALL_CH if (cell & NORTH) else OPEN_CH
        top += WALL_CH  # last corner
        lines.append(top)

        # Cell row
        row = ""
        for x in range(w):
            cell = gen.cells[y][x]
            row += WALL_CH if (cell & WEST) else OPEN_CH
            # Cell interior character
            if (x, y) == (ex, ey):
                row += colours["entry"] + "E" + colours["wall"]
            elif (x, y) == (xx, xy):
                row += colours["exit"] + "X" + colours["wall"]
            elif (x, y) in path_set:
                row += colours["path"] + PATH_CH + colours["wall"]
            elif (x, y) in ft_set:
                row += colours["fortytwo"] + WALL_CH + colours["wall"]
            else:
                row += OPEN_CH
        row += WALL_CH  # east border
        lines.append(row)

    # Bottom border
    bottom = WALL_CH * (w + 1)
    for x in range(w):
        bottom += WALL_CH
    lines.append(WALL_CH * (w + 1))

    _clear()
    wall_c = colours["wall"]
    print(wall_c)
    for line in lines:
        print("  " + line)
    print(ANSI_RESET)


def interactive_loop(
    gen: MazeGenerator,
    config: "MazeConfig",  # type: ignore[name-defined]  # noqa: F821
    output_path: str,
) -> None:
    """Run the interactive terminal menu.

    Args:
        gen: The initial MazeGenerator instance.
        config: Parsed MazeConfig for re-generation.
        output_path: Path to write output file on re-generation.
    """
    from maze_writer import write_output
    from mazegen_pkg.mazegen.generator import MazeGenerator as MG

    show_path: bool = False
    colour_idx: int = 0

    while True:
        render_maze(gen, show_path=show_path, colour_idx=colour_idx)
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze wall colours")
        print("4. Quit")
        choice = input("Choice (1-4): ").strip()

        if choice == "1":
            # Increment seed for reproducibility while still being new
            new_seed: Optional[int] = (
                (config.seed + 1) if config.seed is not None else None
            )
            gen = MG(
                width=config.width,
                height=config.height,
                entry=config.entry,
                exit_=config.exit_,
                seed=new_seed,
            )
            gen.generate(perfect=config.perfect)
            if new_seed is not None:
                config.seed = new_seed
            write_output(gen, output_path)
        elif choice == "2":
            show_path = not show_path
        elif choice == "3":
            colour_idx = (colour_idx + 1) % len(COLOUR_SETS)
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please enter 1-4.")