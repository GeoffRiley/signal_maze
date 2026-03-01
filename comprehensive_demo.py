#!/usr/bin/env python3
"""Comprehensive demonstration of Signal Maze features."""

from signal_maze.grid import Grid
from signal_maze.components import Source, Exit, Mirror, Switch, Blocker, Splitter
from signal_maze.signal import Direction
from signal_maze.game import Game


def demo_feature(title, description, game, moves=None):
    """Helper to demonstrate a feature."""
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)
    print(f"\n{description}\n")
    print(game.display())
    
    if moves:
        for i, (move_desc, func) in enumerate(moves, 1):
            print(f"\n{'-' * 70}")
            print(f"Move {i}: {move_desc}")
            func()
            print(game.display())
    
    print()


def main():
    """Run comprehensive demos."""
    print("\n" + "🎮 " * 20)
    print(" " * 15 + "SIGNAL MAZE - COMPREHENSIVE DEMO")
    print("🎮 " * 20 + "\n")
    
    # Feature 1: Basic signal flow
    grid1 = Grid(10, 5)
    grid1.set_component(1, 2, Source(1, 2, Direction.RIGHT))
    grid1.set_component(8, 2, Exit(8, 2))
    game1 = Game(grid1)
    
    demo_feature(
        "1. Basic Signal Flow",
        "Signal travels in straight line from source (>) to exit (X)",
        game1
    )
    
    # Feature 2: Mirror reflection
    grid2 = Grid(10, 6)
    grid2.set_component(1, 1, Source(1, 1, Direction.RIGHT))
    grid2.set_component(5, 5, Exit(5, 5))
    grid2.set_component(5, 1, Mirror(5, 1, '\\'))
    grid2.set_component(5, 5, Mirror(5, 5, '/'))
    game2 = Game(grid2)
    
    demo_feature(
        "2. Mirror Reflection",
        "Mirrors (/ \\) reflect signals at 90-degree angles",
        game2
    )
    
    # Feature 3: Rotating mirrors
    grid3 = Grid(8, 5)
    grid3.set_component(1, 2, Source(1, 2, Direction.RIGHT))
    grid3.set_component(6, 2, Exit(6, 2))
    grid3.set_component(4, 2, Mirror(4, 2, '\\'))
    game3 = Game(grid3)
    
    demo_feature(
        "3. Rotating Mirrors",
        "Rotate mirrors to guide signals to exits",
        game3,
        [
            ("Rotate mirror at (4, 2)", lambda: game3.rotate_component(4, 2))
        ]
    )
    
    # Feature 4: Switches
    grid4 = Grid(12, 5)
    grid4.set_component(1, 2, Source(1, 2, Direction.RIGHT))
    grid4.set_component(10, 2, Exit(10, 2))
    grid4.set_component(6, 2, Switch(6, 2, False))  # Closed
    game4 = Game(grid4)
    
    demo_feature(
        "4. Switches",
        "Switches control signal flow (○=open, ●=closed)",
        game4,
        [
            ("Toggle switch at (6, 2) to open path", lambda: game4.toggle_component(6, 2))
        ]
    )
    
    # Feature 5: Blockers
    grid5 = Grid(10, 5)
    grid5.set_component(1, 1, Source(1, 1, Direction.RIGHT))
    grid5.set_component(8, 3, Exit(8, 3))
    grid5.set_component(5, 1, Blocker(5, 1))
    grid5.set_component(5, 1, Mirror(5, 1, '\\'))
    grid5.set_component(5, 3, Mirror(5, 3, '/'))
    game5 = Game(grid5)
    
    demo_feature(
        "5. Blockers & Pathfinding",
        "Navigate around blockers (█) using mirrors",
        game5
    )
    
    # Feature 6: Splitters
    grid6 = Grid(12, 7)
    grid6.set_component(1, 3, Source(1, 3, Direction.RIGHT))
    grid6.set_component(6, 3, Splitter(6, 3, 'T'))
    grid6.set_component(6, 1, Exit(6, 1))
    grid6.set_component(6, 5, Exit(6, 5))
    game6 = Game(grid6)
    
    demo_feature(
        "6. Signal Splitters",
        "Splitters (T) divide signals into multiple directions",
        game6
    )
    
    # Feature 7: Multiple sources
    grid7 = Grid(12, 7)
    grid7.set_component(1, 2, Source(1, 2, Direction.RIGHT))
    grid7.set_component(1, 4, Source(1, 4, Direction.RIGHT))
    grid7.set_component(10, 2, Exit(10, 2))
    grid7.set_component(10, 4, Exit(10, 4))
    game7 = Game(grid7)
    
    demo_feature(
        "7. Multiple Sources & Exits",
        "All exits must be reached to win",
        game7
    )
    
    print("=" * 70)
    print("  DEMO COMPLETE")
    print("=" * 70)
    print("\nKey Features Summary:")
    print("  ✓ Turn-based gameplay with move tracking")
    print("  ✓ Signal flow simulation and visualization")
    print("  ✓ Multiple component types (7 types)")
    print("  ✓ Rotatable mirrors and toggleable switches")
    print("  ✓ Loop detection prevents infinite signal paths")
    print("  ✓ Complex multi-source, multi-exit puzzles")
    print("  ✓ Win condition checking")
    print("\nTo play: python main.py")
    print("=" * 70)


if __name__ == '__main__':
    main()
