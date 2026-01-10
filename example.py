#!/usr/bin/env python3
"""Example usage of Signal Maze."""

from signal_maze import SignalMaze


def main():
    """Demonstrate basic usage of SignalMaze."""
    print("Signal Maze Example\n" + "=" * 50)
    
    # Create a simple maze
    grid = [
        ['S', 'E', 'X'],
        ['N', 'E', 'N'],
        ['E', 'N', 'W']
    ]
    
    print("\nMaze layout:")
    maze = SignalMaze(grid)
    print(maze)
    print(f"\nSize: {maze.rows}x{maze.cols}")
    
    # Try to find the exit
    print("\nFinding exit...")
    exit_pos = maze.find_exit()
    if exit_pos:
        print(f"Exit found at position: {exit_pos}")
    else:
        print("No exit found in maze")
    
    # Try to navigate
    print("\nNavigating from (0, 0)...")
    success, path = maze.navigate(0, 0)
    
    if success:
        print(f"✓ Successfully reached exit!")
        print(f"Path taken ({len(path)} steps): {path}")
    else:
        print(f"✗ Failed to reach exit")
        print(f"Path before failure: {path}")


if __name__ == "__main__":
    main()
