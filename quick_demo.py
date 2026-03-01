#!/usr/bin/env python3
"""Quick visual demonstration of Signal Maze gameplay."""

from signal_maze.cli import create_tutorial_level, create_mirror_puzzle


print("="*70)
print(" "*20 + "SIGNAL MAZE - Quick Demo")
print("="*70)
print()

# Tutorial Level
print("TUTORIAL LEVEL - Simple Mirror Puzzle")
print("-"*70)
game = create_tutorial_level()

print("\nBEFORE:")
print(game.display())

print("\nACTION: Rotate mirror at position (4, 1)")
game.rotate_component(4, 1)

print("\nAFTER:")
print(game.display())
print()

# Mirror Puzzle
print("="*70)
print("MIRROR PUZZLE - Navigate Around Obstacles")
print("-"*70)
game2 = create_mirror_puzzle()
print(game2.display())
print()

print("="*70)
print("\nComponents Legend:")
print("  ^ v < >  : Signal sources (emit signals)")
print("  X        : Exits (reach all to win)")
print("  / \\      : Mirrors (reflect signals 90°)")
print("  ○ ●      : Switches (toggle to open/close)")
print("  █        : Blockers (stop signals)")
print("  ↑ ↓ ← →  : Active signals moving")
print("  ·        : Empty wire")
print()
print("Commands: r <x> <y> (rotate) | t <x> <y> (toggle) | h (help) | q (quit)")
print()
print("To play: python main.py")
print("="*70)
