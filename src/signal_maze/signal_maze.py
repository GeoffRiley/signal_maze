"""
Signal Maze - Navigate through a grid by following signal patterns.

In this puzzle, you need to navigate through a grid maze by following signals.
Each cell in the grid contains a signal that tells you which direction to move next.

Signals:
    'N' - Move North (up)
    'S' - Move South (down)
    'E' - Move East (right)
    'W' - Move West (left)
    'X' - Stop (exit found)

Example:
    A simple 3x3 maze:
        S E X
        N E N
        E N W

    Starting at position (0, 0), follow the signals to reach 'X'.
"""

from typing import List, Tuple, Optional


class SignalMaze:
    """A maze that uses signals to guide navigation."""

    DIRECTIONS = {
        'N': (-1, 0),  # North: row - 1
        'S': (1, 0),   # South: row + 1
        'E': (0, 1),   # East: col + 1
        'W': (0, -1),  # West: col - 1
        'X': (0, 0),   # Exit marker
    }

    def __init__(self, grid: List[List[str]]):
        """
        Initialize a Signal Maze with a grid of signals.

        Args:
            grid: A 2D list of strings representing the maze.
                  Each string should be a valid signal ('N', 'S', 'E', 'W', or 'X').

        Raises:
            ValueError: If the grid is empty or contains invalid signals.
        """
        if not grid or not grid[0]:
            raise ValueError("Grid cannot be empty")
        
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # Validate grid
        for row in grid:
            if len(row) != self.cols:
                raise ValueError("All rows must have the same length")
            for cell in row:
                if cell not in self.DIRECTIONS:
                    raise ValueError(f"Invalid signal: {cell}")

    def navigate(self, start_row: int = 0, start_col: int = 0) -> Tuple[bool, List[Tuple[int, int]]]:
        """
        Navigate through the maze starting from the given position.

        Args:
            start_row: Starting row position (default: 0)
            start_col: Starting column position (default: 0)

        Returns:
            A tuple of (success, path) where:
                - success: True if exit ('X') was found, False otherwise
                - path: List of (row, col) positions visited in order

        The navigation stops when:
            - An 'X' signal is encountered (success)
            - The path goes out of bounds (failure)
            - A cycle is detected (visited same position twice) (failure)
        """
        pass  # TODO: Implement this method

    def find_exit(self) -> Optional[Tuple[int, int]]:
        """
        Find the position of the exit ('X') in the maze.

        Returns:
            A tuple of (row, col) if exit is found, None otherwise.
        """
        pass  # TODO: Implement this method

    def is_valid_position(self, row: int, col: int) -> bool:
        """
        Check if a position is within the maze bounds.

        Args:
            row: Row position
            col: Column position

        Returns:
            True if position is valid, False otherwise.
        """
        pass  # TODO: Implement this method

    def get_signal(self, row: int, col: int) -> Optional[str]:
        """
        Get the signal at a specific position.

        Args:
            row: Row position
            col: Column position

        Returns:
            The signal character at the position, or None if position is invalid.
        """
        pass  # TODO: Implement this method

    def __str__(self) -> str:
        """Return a string representation of the maze."""
        return '\n'.join([' '.join(row) for row in self.grid])
