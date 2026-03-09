*This project has been created as part of the 42 curriculum by \<login\>.*

# A-Maze-ing

## Description

A-Maze-ing is a Python maze generator and interactive terminal visualiser.
It generates mazes using the **recursive backtracker (DFS)** algorithm, supporting both **perfect** mazes (unique path between any two cells) and **imperfect** mazes (with loops). The maze contains a hidden **"42"** pattern made of fully-closed cells. The output is a hexadecimal file encoding each cell's walls.

## Instructions

### Requirements

- Python 3.10+
- No external dependencies for core execution

### Install tools (linting/building)

```bash
make install
```

### Run

```bash
python3 a_maze_ing.py config.txt
```

### Debug

```bash
make debug
```

### Lint

```bash
make lint
```

### Clean

```bash
make clean
```

## Configuration file format

```
# Lines starting with # are comments
WIDTH=20          # Maze width in cells (>= 2)
HEIGHT=15         # Maze height in cells (>= 2)
ENTRY=0,0         # Entry coordinates x,y
EXIT=19,14        # Exit coordinates x,y
OUTPUT_FILE=maze.txt  # Output file path
PERFECT=True      # True = perfect maze, False = imperfect (loops)
SEED=42           # Optional random seed for reproducibility
ALGORITHM=dfs     # Generation algorithm (currently: dfs)
```

## Maze generation algorithm

**Recursive Backtracker (DFS)**

Starting from the entry cell, the algorithm:
1. Marks the current cell as visited.
2. Picks a random unvisited neighbour.
3. Removes the wall between them and recurses.
4. Backtracks when no unvisited neighbours remain.

### Why DFS?

- Produces long, winding corridors — mazes feel complex and interesting.
- Simple to implement and reason about.
- Naturally produces a perfect maze (spanning tree of the cell graph).
- Easy to seed for reproducibility.

## Visual representation (terminal)

The terminal display uses ANSI block characters. Interactive options:

| Key | Action |
|-----|--------|
| 1   | Re-generate a new maze |
| 2   | Show/Hide shortest path |
| 3   | Rotate wall colour scheme |
| 4   | Quit |

## Reusable module

The maze generation logic is packaged as `mazegen` (see `mazegen_pkg/`).

### Install the package

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

### Build from source

```bash
cd mazegen_pkg
pip install build
python -m build
```

### API example

```python
from mazegen import MazeGenerator

gen = MazeGenerator(width=20, height=15, seed=42)
gen.generate(perfect=True)

# Access cell walls (bitmask: N=1, E=2, S=4, W=8)
walls = gen.cells[0][0]

# Get shortest path string
path = gen.get_solution()   # e.g. "NEESSWWN..."

# Get 42-pattern cell positions
pattern = gen.forty_two_cells
```

## Resources

- [Maze generation algorithms – Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive backtracker explanation – weblog.jamisbuck.org](http://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker)
- [Python `random` module docs](https://docs.python.org/3/library/random.html)
- [BFS pathfinding – Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)

### AI usage

Claude (Anthropic) was used to assist with: boilerplate for the pyproject.toml packaging setup, the ANSI colour rendering loop, and the BFS pathfinding logic. All code was reviewed, tested, and understood before inclusion.

## Team and project management

| Member | Role |
|--------|------|
| \<login\> | Sole developer |

**Planning:** Initial plan was 3 days — generator core (day 1), output format + pathfinding (day 2), display + packaging (day 3). Actual time matched the estimate.

**What worked well:** The DFS algorithm was straightforward to implement and test. The hex output format was well-specified.

**What could be improved:** Adding a graphical MLX display would improve the visual experience. Supporting multiple algorithms (Prim's, Kruskal's) would be a useful bonus.

**Tools used:** Python 3.12, flake8, mypy, build (pip package).