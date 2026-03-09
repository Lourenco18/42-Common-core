"""A-Maze-ing: maze generator and terminal display.

Usage:
    python3 a_maze_ing.py config.txt
"""

import sys

from config_parser import parse_config
from maze_display import interactive_loop
from maze_writer import write_output
from mazegen_pkg.mazegen.generator import MazeGenerator


def main() -> None:
    """Parse config, generate maze, write output and start display."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>", file=sys.stderr)
        sys.exit(1)

    config = parse_config(sys.argv[1])

    gen = MazeGenerator(
        width=config.width,
        height=config.height,
        entry=config.entry,
        exit_=config.exit_,
        seed=config.seed,
    )
    gen.generate(perfect=config.perfect)

    write_output(gen, config.output_file)
    print(f"Maze written to '{config.output_file}'.")

    interactive_loop(gen, config, config.output_file)


if __name__ == "__main__":
    main()
