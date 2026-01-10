"""Example solution for Signal Maze - for testing purposes."""

# This file contains an example implementation for testing.
# Students should implement their own solution in signal_maze.py

from typing import List, Tuple, Optional


class SignalMazeSolution:
    """Example solution for Signal Maze."""

    DIRECTIONS = {
        'N': (-1, 0),
        'S': (1, 0),
        'E': (0, 1),
        'W': (0, -1),
        'X': (0, 0),
    }

    def __init__(self, grid: List[List[str]]):
        if not grid or not grid[0]:
            raise ValueError("Grid cannot be empty")
        
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        for row in grid:
            if len(row) != self.cols:
                raise ValueError("All rows must have the same length")
            for cell in row:
                if cell not in self.DIRECTIONS:
                    raise ValueError(f"Invalid signal: {cell}")

    def navigate(self, start_row: int = 0, start_col: int = 0) -> Tuple[bool, List[Tuple[int, int]]]:
        path = []
        visited = set()
        row, col = start_row, start_col
        
        while True:
            if not self.is_valid_position(row, col):
                return False, path
            
            path.append((row, col))
            
            signal = self.get_signal(row, col)
            if signal == 'X':
                return True, path
            
            if (row, col) in visited:
                return False, path
            
            visited.add((row, col))
            
            dr, dc = self.DIRECTIONS[signal]
            row += dr
            col += dc

    def find_exit(self) -> Optional[Tuple[int, int]]:
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == 'X':
                    return (i, j)
        return None

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def get_signal(self, row: int, col: int) -> Optional[str]:
        if not self.is_valid_position(row, col):
            return None
        return self.grid[row][col]

    def __str__(self) -> str:
        return '\n'.join([' '.join(row) for row in self.grid])
