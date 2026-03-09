"""Write maze to output file in hexadecimal format."""

import sys
from mazegen_pkg.mazegen.generator import MazeGenerator


def write_output(gen: MazeGenerator, path: str) -> None:
    """Write maze to file: hex grid + entry + exit + solution path.

    Args:
        gen: A MazeGenerator instance after generate() has been called.
        path: Output file path.
    """
    ex, ey = gen.entry
    xx, xy = gen.exit_
    solution = gen.get_solution()

    try:
        with open(path, "w", encoding="utf-8") as fh:
            # Hex grid, one row per line
            for row in gen.cells:
                fh.write("".join(f"{cell:X}" for cell in row) + "\n")
            # Empty line separator
            fh.write("\n")
            # Entry coordinates
            fh.write(f"{ex},{ey}\n")
            # Exit coordinates
            fh.write(f"{xx},{xy}\n")
            # Shortest path
            fh.write(solution + "\n")
    except OSError as exc:
        print(f"[ERROR] Cannot write output file: {exc}", file=sys.stderr)
        sys.exit(1)