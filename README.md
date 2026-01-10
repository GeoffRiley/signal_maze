# Signal Maze

A game of signals and a grid of problems.

## Description

Signal Maze is a programming exercise where you navigate through a grid by following directional signals. Each cell in the grid contains a signal that tells you which direction to move next.

### Signals

- `N` - Move North (up)
- `S` - Move South (down)
- `E` - Move East (right)
- `W` - Move West (left)
- `X` - Stop (exit found)

### Example

A simple 3x3 maze:
```
S E X
N E N
E N W
```

Starting at position (0, 0), follow the signals:
1. Start at (0, 0) with signal 'S' → move South to (1, 0)
2. At (1, 0) with signal 'N' → move North to (0, 0)
3. ...and so on until you reach 'X'

## Installation

```bash
pip install -e .
```

For development:
```bash
pip install -e ".[dev]"
```

## Usage

```python
from signal_maze import SignalMaze

# Create a maze
grid = [
    ['S', 'E', 'X'],
    ['N', 'E', 'N'],
    ['E', 'N', 'W']
]
maze = SignalMaze(grid)

# Navigate from the top-left corner
success, path = maze.navigate(0, 0)

if success:
    print(f"Exit found! Path: {path}")
else:
    print("Could not reach the exit")
```

## Your Task

Implement the following methods in `src/signal_maze/signal_maze.py`:

1. `navigate(start_row, start_col)` - Navigate through the maze and return whether the exit was found and the path taken
2. `find_exit()` - Find the position of the exit in the maze
3. `is_valid_position(row, col)` - Check if a position is within bounds
4. `get_signal(row, col)` - Get the signal at a specific position

## Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=signal_maze tests/
```

## Rules

- Navigation stops when:
  - An 'X' signal is encountered (success)
  - The path goes out of bounds (failure)
  - A cycle is detected (visiting the same position twice) (failure)

## License

GNU General Public License v3.0 - see LICENSE file for details.
