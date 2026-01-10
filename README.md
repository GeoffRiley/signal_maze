# Signal Maze

A turn-based puzzle game played on a grid of interconnected components. Guide signals from sources to exits by manipulating the environment!

## About

Signal Maze is a puzzle game where you must guide one or more signals from their sources to specific exits by changing the environment. You can rotate mirrors, toggle switches, and strategically plan your moves. Signals obey strict logical rules, reflecting, splitting, or terminating depending on what they encounter. Each move recalculates the entire signal flow, creating a dynamic puzzle where small changes ripple through the system.

## Features

- **Turn-based gameplay**: Plan your moves carefully
- **Multiple component types**:
  - Sources (^ v < >) - Emit signals in a direction
  - Exits (X) - Target destinations for signals
  - Mirrors (/ \\) - Reflect signals at 90-degree angles
  - Switches (○ ●) - Toggle to allow or block signal flow
  - Blockers (█) - Fixed obstacles that stop signals
  - Splitters (+ T) - Split signals into multiple directions
  - Wires (·) - Allow signals to pass through
- **Signal visualization**: See signals as arrows (↑ ↓ ← →) flowing through the grid
- **Multiple puzzle levels**: From simple tutorials to complex challenges
- **Move counter**: Track your efficiency

## Installation

```bash
# Clone the repository
git clone https://github.com/GeoffRiley/signal_maze.git
cd signal_maze

# Install the package
pip install -e .
```

## Usage

### Play the game

```bash
# Run directly
python main.py

# Or use the installed command
signal-maze
```

### Game Commands

- `r <x> <y>` - Rotate component at position (x, y)
- `t <x> <y>` - Toggle component at position (x, y)
- `h` - Show help
- `q` - Quit game

### Example Gameplay

```
┌────────────┐
│·^·····X···│
│············│
│·····\······│
│············│
│············│
│············│
└────────────┘

Moves: 0
Exits reached: 0/1
```

Rotate the mirror to guide the signal to the exit!

## Running Tests

```bash
python tests/test_signal_maze.py
```

## How It Works

1. **Sources** emit signals in a fixed direction at the start of each turn
2. **Signals** travel through the grid one step at a time
3. When signals encounter **components**, they interact according to rules:
   - Mirrors reflect signals 90 degrees
   - Switches allow or block signals based on their state
   - Splitters divide signals into multiple directions
   - Exits capture signals (goal is to reach all exits)
4. After each move, the entire signal flow is recalculated
5. The puzzle is solved when all exits are reached

## Development

### Project Structure

```
signal_maze/
├── signal_maze/          # Main package
│   ├── __init__.py      # Package initialization
│   ├── signal.py        # Signal and Direction classes
│   ├── components.py    # Game components (Source, Exit, Mirror, etc.)
│   ├── grid.py          # Grid management
│   ├── game.py          # Game logic and state management
│   └── cli.py           # Command-line interface
├── tests/               # Test suite
│   └── test_signal_maze.py
├── main.py              # Entry point
├── setup.py             # Package configuration
└── README.md            # This file
```

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Feel free to:
- Add new puzzle levels
- Create new component types
- Improve the UI
- Fix bugs or add features

## Author

Geoff Riley
