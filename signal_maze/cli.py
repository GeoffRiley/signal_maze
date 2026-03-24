"""Command-line interface for Signal Maze."""

from typing import Optional

from .components import Source, Exit, Mirror, Switch, Blocker, Splitter
from .game import Game
from .grid import Grid
from .signal import Direction


def create_tutorial_level() -> Game:
    """Create a simple tutorial level."""
    grid = Grid(8, 6)

    # Place source pointing right and exit at the bottom
    grid.set_component(1, 1, Source(1, 1, Direction.RIGHT))
    grid.set_component(6, 4, Exit(6, 4))

    # Place mirrors - player needs to create a path: right -> down -> right
    grid.set_component(4, 1, Mirror(4, 1, '/'))  # Wrong, should be \
    grid.set_component(4, 4, Mirror(4, 4, '\\'))  # Wrong, should be /

    return Game(grid)


def create_mirror_puzzle() -> Game:
    """Create a puzzle with mirrors."""
    grid = Grid(12, 8)

    # Source at top-left
    grid.set_component(1, 1, Source(1, 1, Direction.RIGHT))

    # Exit at bottom-right
    grid.set_component(10, 6, Exit(10, 6))

    # Mirrors to guide the signal
    grid.set_component(5, 1, Mirror(5, 1, '\\'))
    grid.set_component(5, 5, Mirror(5, 5, '/'))
    grid.set_component(10, 5, Mirror(10, 5, '\\'))

    # Blockers
    grid.set_component(3, 3, Blocker(3, 3))
    grid.set_component(7, 4, Blocker(7, 4))

    return Game(grid)


def create_switch_puzzle() -> Game:
    """Create a puzzle with switches."""
    grid = Grid(15, 8)

    # Two sources
    grid.set_component(1, 2, Source(1, 2, Direction.RIGHT))
    grid.set_component(1, 5, Source(1, 5, Direction.RIGHT))

    # Two exits
    grid.set_component(13, 2, Exit(13, 2))
    grid.set_component(13, 5, Exit(13, 5))

    # Switches to control paths
    grid.set_component(7, 2, Switch(7, 2, False))  # Initially closed
    grid.set_component(7, 5, Switch(7, 5, True))  # Initially open

    # Mirrors
    grid.set_component(4, 2, Mirror(4, 2, '/'))
    grid.set_component(10, 5, Mirror(10, 5, '\\'))

    return Game(grid)


def create_complex_puzzle() -> Game:
    """Create a complex puzzle with multiple components."""
    grid = Grid(16, 10)

    # Sources
    grid.set_component(2, 2, Source(2, 2, Direction.RIGHT))
    grid.set_component(13, 7, Source(13, 7, Direction.LEFT))

    # Exits
    grid.set_component(13, 2, Exit(13, 2))
    grid.set_component(2, 7, Exit(2, 7))

    # Mirrors
    grid.set_component(6, 2, Mirror(6, 2, '\\'))
    grid.set_component(6, 5, Mirror(6, 5, '/'))
    grid.set_component(9, 5, Mirror(9, 5, '\\'))
    grid.set_component(9, 2, Mirror(9, 2, '/'))

    # Switches
    grid.set_component(4, 4, Switch(4, 4, False))
    grid.set_component(11, 4, Switch(11, 4, True))

    # Blockers
    grid.set_component(7, 7, Blocker(7, 7))
    grid.set_component(8, 7, Blocker(8, 7))

    # Splitter
    grid.set_component(7, 4, Splitter(7, 4, 'T'))

    return Game(grid)


LEVELS = {
    '1': ('Tutorial', create_tutorial_level),
    '2': ('Mirror Puzzle', create_mirror_puzzle),
    '3': ('Switch Puzzle', create_switch_puzzle),
    '4': ('Complex Puzzle', create_complex_puzzle),
}


def print_help():
    """Print help information."""
    print("\nCommands:")
    print("  r <x> <y>  - Rotate component at position (x, y)")
    print("  t <x> <y>  - Toggle component at position (x, y)")
    print("  h          - Show this help")
    print("  q          - Quit game")
    print("\nComponents:")
    print("  ^ v < >  - Signal sources (emit signals)")
    print("  X        - Exit (signals must reach all exits)")
    print("  / \\      - Mirrors (reflect signals)")
    print("  ○ ●      - Switches (○=open, ●=closed)")
    print("  █        - Blockers (stop signals)")
    print("  + T      - Splitters (split signals)")
    print("  ·        - Wire (signals pass through)")
    print("\nSignals are shown as arrows: ↑ ↓ ← →")


def select_level() -> Optional[Game]:
    """Let the player select a level."""
    print("\n=== Signal Maze ===")
    print("\nAvailable levels:")
    for key, (name, _) in LEVELS.items():
        print(f"  {key}. {name}")

    choice = input("\nSelect a level (1-4) or 'q' to quit: ").strip()

    if choice.lower() == 'q':
        return None

    if choice in LEVELS:
        _, create_func = LEVELS[choice]
        return create_func()

    print("Invalid selection!")
    return select_level()


def play_game(game: Game):
    """Main game loop."""
    print("\n" + "=" * 50)
    print(game.display())
    print_help()

    while True:
        command = input("\nEnter command: ").strip().lower()

        if not command:
            continue

        parts = command.split()
        cmd = parts[0]

        if cmd == 'q':
            print("Thanks for playing!")
            break

        elif cmd == 'h':
            print_help()
            continue

        elif cmd == 'r' and len(parts) == 3:
            try:
                x, y = int(parts[1]), int(parts[2])
                if game.rotate_component(x, y):
                    print(f"Rotated component at ({x}, {y})")
                else:
                    print(f"Cannot rotate component at ({x}, {y})")
            except ValueError:
                print("Invalid coordinates! Use: r <x> <y>")

        elif cmd == 't' and len(parts) == 3:
            try:
                x, y = int(parts[1]), int(parts[2])
                if game.toggle_component(x, y):
                    print(f"Toggled component at ({x}, {y})")
                else:
                    print(f"Cannot toggle component at ({x}, {y})")
            except ValueError:
                print("Invalid coordinates! Use: t <x> <y>")

        else:
            print("Invalid command! Type 'h' for help.")
            continue

        # Display the updated game state
        print("\n" + "=" * 50)
        print(game.display())

        # Check win condition
        if game.check_win_condition():
            print(f"\n🎉 Level complete in {game.move_count} moves! 🎉")

            play_again = input("\nPlay another level? (y/n): ").strip().lower()
            if play_again == 'y':
                if new_game := select_level():
                    play_game(new_game)
            break


def main():
    """Main entry point."""
    try:
        if game := select_level():
            play_game(game)
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
