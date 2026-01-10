#!/usr/bin/env python3
"""Demonstration of Signal Maze gameplay."""

from signal_maze.cli import create_tutorial_level, create_mirror_puzzle, create_switch_puzzle


def demo_tutorial():
    """Demonstrate the tutorial level."""
    print("="*70)
    print("DEMO: Tutorial Level")
    print("="*70)
    
    game = create_tutorial_level()
    
    print("\n1. Initial State:")
    print(game.display())
    print("\nThe signal goes up instead of down to reach the exit.")
    
    print("\n" + "-"*70)
    print("2. Rotating mirror at (4, 1) to redirect signal downward:")
    game.rotate_component(4, 1)
    print(game.display())
    
    if game.check_win_condition():
        print(f"\n✅ Puzzle solved in {game.move_count} move!")
    
    print("\n")


def demo_mirror_puzzle():
    """Demonstrate a more complex mirror puzzle."""
    print("="*70)
    print("DEMO: Mirror Puzzle")
    print("="*70)
    
    game = create_mirror_puzzle()
    
    print("\n1. Initial State:")
    print(game.display())
    print("\nThe signal needs to navigate around blockers to reach the exit.")
    print(f"Current exits reached: {sum(1 for e in game.exits if e.reached)}/{len(game.exits)}")
    
    print("\n")


def demo_switch_puzzle():
    """Demonstrate the switch puzzle."""
    print("="*70)
    print("DEMO: Switch Puzzle")
    print("="*70)
    
    game = create_switch_puzzle()
    
    print("\n1. Initial State:")
    print(game.display())
    print("\nTwo sources need to reach their respective exits.")
    print("Switches control which paths are open.")
    print(f"Current exits reached: {sum(1 for e in game.exits if e.reached)}/{len(game.exits)}")
    
    print("\n" + "-"*70)
    print("2. Toggle switch at (7, 2) to open first path:")
    game.toggle_component(7, 2)
    print(game.display())
    print(f"Exits reached: {sum(1 for e in game.exits if e.reached)}/{len(game.exits)}")
    
    if game.check_win_condition():
        print(f"\n✅ Both exits reached in {game.move_count} move!")
    
    print("\n")


def main():
    """Run all demonstrations."""
    print("\n" + "🎮 "*20)
    print(" "*20 + "SIGNAL MAZE - GAME DEMO")
    print("🎮 "*20 + "\n")
    
    print("Signal Maze is a turn-based puzzle game where you guide signals")
    print("from sources to exits by manipulating components on a grid.")
    print("\nComponents:")
    print("  ^ v < >  : Signal sources")
    print("  X        : Exits (goal destinations)")
    print("  / \\      : Mirrors (reflect signals 90°)")
    print("  ○ ●      : Switches (○=open, ●=closed)")
    print("  █        : Blockers (stop signals)")
    print("  ↑ ↓ ← →  : Active signals")
    print()
    
    input("Press Enter to start demos...")
    print()
    
    demo_tutorial()
    input("Press Enter for next demo...")
    
    demo_mirror_puzzle()
    input("Press Enter for next demo...")
    
    demo_switch_puzzle()
    
    print("="*70)
    print("DEMO COMPLETE")
    print("="*70)
    print("\nTo play the game yourself, run:")
    print("  python main.py")
    print("or:")
    print("  signal-maze  (after installation)")
    print()


if __name__ == '__main__':
    main()
