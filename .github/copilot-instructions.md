# Copilot instructions for Signal Maze

## Project overview
- Signal Maze is a turn-based puzzle game where signals propagate through a 2D grid of components.
- Core package: `/home/runner/work/signal_maze/signal_maze/signal_maze`
- Game rules and mechanics are documented in `/home/runner/work/signal_maze/signal_maze/MECHANICS.md`.

## Repository expectations
- Keep changes focused and minimal for the requested issue.
- Preserve existing gameplay behavior unless the issue explicitly asks for behavior changes.
- Follow existing Python style in nearby files; avoid introducing new dependencies unless required.

## Validation
- Run tests with:
  - `python tests/test_signal_maze.py`

## Typical entry points
- CLI/game entry point: `/home/runner/work/signal_maze/signal_maze/main.py`
- Main game logic: `/home/runner/work/signal_maze/signal_maze/signal_maze/game.py`
- Components: `/home/runner/work/signal_maze/signal_maze/signal_maze/components.py`
- Grid and signal propagation: `/home/runner/work/signal_maze/signal_maze/signal_maze/grid.py`, `/home/runner/work/signal_maze/signal_maze/signal_maze/signal.py`
