"""Maze generator module using recursive backtracker (DFS) algorithm.

This module provides the MazeGenerator class for generating perfect or
imperfect mazes with a hexadecimal wall representation.

Example:
    >>> from mazegen.generator import MazeGenerator
    >>> gen = MazeGenerator(width=20, height=15, seed=42)
    >>> gen.generate(perfect=True)
    >>> print(gen.get_solution())
    >>> cells = gen.cells  # 2D list of wall bitmasks
"""

import random
from collections import deque
from typing import Optional


# Wall bitmask constants (bits: 0=N, 1=E, 2=S, 3=W)
NORTH: int = 0x1
EAST: int = 0x2
SOUTH: int = 0x4
WEST: int = 0x8
ALL_WALLS: int = NORTH | EAST | SOUTH | WEST

OPPOSITE: dict[int, int] = {
    NORTH: SOUTH,
    EAST: WEST,
    SOUTH: NORTH,
    WEST: EAST,
}

DIRECTION_DELTA: dict[int, tuple[int, int]] = {
    NORTH: (0, -1),
    EAST: (1, 0),
    SOUTH: (0, 1),
    WEST: (-1, 0),
}

DIR_LETTER: dict[int, str] = {
    NORTH: "N",
    EAST: "E",
    SOUTH: "S",
    WEST: "W",
}

# "42" pixel font patterns (each digit as list of (col, row) offsets)
# Each char is 3 cols wide x 5 rows tall
_DIGIT_4: list[tuple[int, int]] = [
    (0, 0), (0, 1), (0, 2),
    (1, 2),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
]
_DIGIT_2: list[tuple[int, int]] = [
    (0, 0), (1, 0), (2, 0),
    (2, 1),
    (0, 2), (1, 2), (2, 2),
    (0, 3),
    (0, 4), (1, 4), (2, 4),
]
# "42" = digit4 at col 0, digit2 at col 4 (gap of 1)
_PATTERN_42: list[tuple[int, int]] = (
    _DIGIT_4 + [(c + 4, r) for c, r in _DIGIT_2]
)
_PATTERN_WIDTH: int = 7   # 3 + 1 gap + 3
_PATTERN_HEIGHT: int = 5


class MazeGenerator:
    """Generate mazes using recursive backtracker (DFS).

    Args:
        width: Number of cells horizontally (>= 2).
        height: Number of cells vertically (>= 2).
        entry: (x, y) entry cell coordinates.
        exit_: (x, y) exit cell coordinates.
        seed: Random seed for reproducibility.

    Attributes:
        cells: 2D list [y][x] of wall bitmasks after generate().
        width: Maze width in cells.
        height: Maze height in cells.
    """

    def __init__(
        self,
        width: int = 20,
        height: int = 15,
        entry: tuple[int, int] = (0, 0),
        exit_: tuple[int, int] = (19, 14),
        seed: Optional[int] = None,
    ) -> None:
        """Initialise the maze generator."""
        if width < 2 or height < 2:
            raise ValueError("Maze must be at least 2x2.")
        ex, ey = entry
        xx, xy = exit_
        if not (0 <= ex < width and 0 <= ey < height):
            raise ValueError(f"Entry {entry} out of bounds.")
        if not (0 <= xx < width and 0 <= xy < height):
            raise ValueError(f"Exit {exit_} out of bounds.")
        if entry == exit_:
            raise ValueError("Entry and exit must be different cells.")

        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = entry
        self.exit_: tuple[int, int] = exit_
        self.seed: Optional[int] = seed
        # cells[y][x] = bitmask of CLOSED walls
        self.cells: list[list[int]] = [
            [ALL_WALLS] * width for _ in range(height)
        ]
        self._forty_two_cells: list[tuple[int, int]] = []
        self._rng: random.Random = random.Random(seed)
        self._generated: bool = False

    def generate(self, perfect: bool = True) -> None:
        """Generate the maze.

        Args:
            perfect: If True, produces a perfect maze (unique path
                between every pair of cells).
        """
        self.cells = [[ALL_WALLS] * self.width for _ in range(self.height)]
        self._forty_two_cells = []
        self._generated = False

        self._place_42_pattern()
        if perfect:
            self._generate_perfect()
        else:
            self._generate_imperfect()

        self._enforce_borders()
        self._open_entry_exit()
        self._generated = True

    def get_solution(self) -> str:
        """Return shortest path from entry to exit as N/E/S/W string.

        Returns:
            A string like "NESSWW..." or empty string if no path.
        """
        if not self._generated:
            raise RuntimeError("Call generate() before get_solution().")
        path = self._bfs_path(self.entry, self.exit_)
        return path

    @property
    def forty_two_cells(self) -> list[tuple[int, int]]:
        """Return list of (x,y) cells that form the '42' pattern."""
        return list(self._forty_two_cells)

    # ------------------------------------------------------------------
    # Internal generation
    # ------------------------------------------------------------------

    def _remove_wall(self, x: int, y: int, direction: int) -> None:
        """Remove wall between (x,y) and its neighbour in direction."""
        dx, dy = DIRECTION_DELTA[direction]
        nx, ny = x + dx, y + dy
        self.cells[y][x] &= ~direction
        self.cells[ny][nx] &= ~OPPOSITE[direction]

    def _in_bounds(self, x: int, y: int) -> bool:
        """Return True if (x, y) is inside the maze grid."""
        return 0 <= x < self.width and 0 <= y < self.height

    def _generate_perfect(self) -> None:
        """Recursive backtracker DFS to carve a perfect maze."""
        visited: list[list[bool]] = [
            [False] * self.width for _ in range(self.height)
        ]
        # Mark 42-pattern cells as visited so DFS skips them
        for cx, cy in self._forty_two_cells:
            visited[cy][cx] = True

        sx, sy = self.entry
        stack: list[tuple[int, int]] = [(sx, sy)]
        visited[sy][sx] = True

        while stack:
            x, y = stack[-1]
            dirs = list(DIRECTION_DELTA.keys())
            self._rng.shuffle(dirs)
            moved = False
            for d in dirs:
                dx, dy = DIRECTION_DELTA[d]
                nx, ny = x + dx, y + dy
                if self._in_bounds(nx, ny) and not visited[ny][nx]:
                    self._remove_wall(x, y, d)
                    visited[ny][nx] = True
                    stack.append((nx, ny))
                    moved = True
                    break
            if not moved:
                stack.pop()

        # Connect any unvisited cells (can happen if 42 blocks paths)
        self._connect_unreachable(visited)

    def _connect_unreachable(
        self, visited: list[list[bool]]
    ) -> None:
        """Connect any isolated cells that DFS could not reach."""
        for y in range(self.height):
            for x in range(self.width):
                if not visited[y][x]:
                    # Find a visited neighbour and connect
                    dirs = list(DIRECTION_DELTA.keys())
                    self._rng.shuffle(dirs)
                    for d in dirs:
                        dx, dy = DIRECTION_DELTA[d]
                        nx, ny = x + dx, y + dy
                        if self._in_bounds(nx, ny) and visited[ny][nx]:
                            self._remove_wall(x, y, d)
                            visited[y][x] = True
                            break

    def _generate_imperfect(self) -> None:
        """Generate imperfect maze: run DFS then add extra openings."""
        self._generate_perfect()
        # Add ~15% extra openings (loops) for imperfect maze
        extra: int = max(1, (self.width * self.height) // 7)
        attempts: int = 0
        opened: int = 0
        while opened < extra and attempts < extra * 10:
            attempts += 1
            x = self._rng.randint(0, self.width - 2)
            y = self._rng.randint(0, self.height - 2)
            d = self._rng.choice(list(DIRECTION_DELTA.keys()))
            dx, dy = DIRECTION_DELTA[d]
            nx, ny = x + dx, y + dy
            if not self._in_bounds(nx, ny):
                continue
            # Don't open 42-pattern walls
            if (x, y) in self._forty_two_cells:
                continue
            if (nx, ny) in self._forty_two_cells:
                continue
            # Don't open if it would create a 3x3 open area
            if self._cells[y][x] & d:
                if not self._would_create_large_open(x, y, d):
                    self._remove_wall(x, y, d)
                    opened += 1

    @property
    def _cells(self) -> list[list[int]]:
        """Alias for self.cells used internally."""
        return self.cells

    def _would_create_large_open(
        self, x: int, y: int, direction: int
    ) -> bool:
        """Return True if removing this wall would create a 3x3 open area."""
        dx, dy = DIRECTION_DELTA[direction]
        nx, ny = x + dx, y + dy
        # Check a 3x3 neighbourhood around both cells
        for cy in range(max(0, y - 1), min(self.height, y + 2)):
            for cx in range(max(0, x - 1), min(self.width, x + 2)):
                open_count = 0
                for ry in range(cy, min(self.height, cy + 3)):
                    for rx in range(cx, min(self.width, cx + 3)):
                        if self._is_fully_open_around(rx, ry, nx, ny, x, y):
                            open_count += 1
                if open_count >= 9:
                    return True
        return False

    def _is_fully_open_around(
        self,
        rx: int, ry: int,
        nx: int, ny: int,
        ox: int, oy: int,
    ) -> bool:
        """Heuristic: check if removing wall keeps open-area constraint."""
        # Simplified check: just count walls of cells near the removed wall
        walls = self.cells[ry][rx]
        if (rx, ry) in [(nx, ny), (ox, oy)]:
            walls &= ~(NORTH | EAST | SOUTH | WEST)  # treat as open
        return walls == 0

    def _place_42_pattern(self) -> None:
        """Place '42' as fully-closed cells if maze is large enough."""
        min_w = _PATTERN_WIDTH + 4
        min_h = _PATTERN_HEIGHT + 4
        if self.width < min_w or self.height < min_h:
            print(
                "Warning: maze too small to display '42' pattern. "
                "Increase WIDTH and HEIGHT."
            )
            return

        # Centre the pattern with some margin from borders
        start_x = (self.width - _PATTERN_WIDTH) // 2
        start_y = (self.height - _PATTERN_HEIGHT) // 2
        # Avoid entry/exit
        ex, ey = self.entry
        xx, xy = self.exit_

        for col, row in _PATTERN_42:
            cx = start_x + col
            cy = start_y + row
            if (cx, cy) in [(ex, ey), (xx, xy)]:
                continue
            self._forty_two_cells.append((cx, cy))

    def _enforce_borders(self) -> None:
        """Ensure all border cells have walls on their outer sides."""
        for x in range(self.width):
            self.cells[0][x] |= NORTH
            self.cells[self.height - 1][x] |= SOUTH
        for y in range(self.height):
            self.cells[y][0] |= WEST
            self.cells[y][self.width - 1] |= EAST

    def _open_entry_exit(self) -> None:
        """Open the entry/exit on the maze border."""
        ex, ey = self.entry
        xx, xy = self.exit_

        # Open entry: prefer border wall; default North if interior
        if ey == 0:
            self.cells[ey][ex] &= ~NORTH
        elif ex == 0:
            self.cells[ey][ex] &= ~WEST
        elif ey == self.height - 1:
            self.cells[ey][ex] &= ~SOUTH
        else:
            self.cells[ey][ex] &= ~EAST

        # Open exit similarly
        if xy == self.height - 1:
            self.cells[xy][xx] &= ~SOUTH
        elif xx == self.width - 1:
            self.cells[xy][xx] &= ~EAST
        elif xy == 0:
            self.cells[xy][xx] &= ~NORTH
        else:
            self.cells[xy][xx] &= ~WEST

    # ------------------------------------------------------------------
    # Pathfinding
    # ------------------------------------------------------------------

    def _bfs_path(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
    ) -> str:
        """BFS to find shortest path from start to end.

        Returns:
            Direction string (N/E/S/W) or empty string if unreachable.
        """
        sx, sy = start
        ex, ey = end
        prev: dict[tuple[int, int], Optional[tuple[tuple[int, int], int]]]
        prev = {(sx, sy): None}
        queue: deque[tuple[int, int]] = deque([(sx, sy)])

        while queue:
            x, y = queue.popleft()
            if (x, y) == (ex, ey):
                break
            for d, (dx, dy) in DIRECTION_DELTA.items():
                nx, ny = x + dx, y + dy
                if (
                    self._in_bounds(nx, ny)
                    and (nx, ny) not in prev
                    and not (self.cells[y][x] & d)
                ):
                    prev[(nx, ny)] = ((x, y), d)
                    queue.append((nx, ny))

        if (ex, ey) not in prev:
            return ""

        # Reconstruct
        path_dirs: list[str] = []
        cur: tuple[int, int] = (ex, ey)
        while prev[cur] is not None:
            parent_info = prev[cur]
            assert parent_info is not None
            parent, d = parent_info
            path_dirs.append(DIR_LETTER[d])
            cur = parent
        path_dirs.reverse()
        return "".join(path_dirs)