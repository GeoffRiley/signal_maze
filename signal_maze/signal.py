"""Signal and direction handling for the Signal Maze game."""

from enum import Enum
from typing import Tuple


class Direction(Enum):
    """Cardinal directions for signal movement."""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def opposite(self) -> 'Direction':
        """Get the opposite direction."""
        opposites = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }
        return opposites[self]

    def rotate_cw(self) -> 'Direction':
        """Rotate direction 90 degrees clockwise."""
        rotations = {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
        }
        return rotations[self]

    def rotate_ccw(self) -> 'Direction':
        """Rotate direction 90 degrees counter-clockwise."""
        rotations = {
            Direction.UP: Direction.LEFT,
            Direction.LEFT: Direction.DOWN,
            Direction.DOWN: Direction.RIGHT,
            Direction.RIGHT: Direction.UP,
        }
        return rotations[self]


class Signal:
    """Represents a signal moving through the grid."""
    
    def __init__(self, x: int, y: int, direction: Direction):
        """Initialize a signal at position (x, y) moving in direction."""
        self.x = x
        self.y = y
        self.direction = direction
    
    def move(self) -> Tuple[int, int]:
        """Move signal in its current direction and return new position."""
        dx, dy = self.direction.value
        self.x += dx
        self.y += dy
        return (self.x, self.y)
    
    def peek_next(self) -> Tuple[int, int]:
        """Get next position without moving."""
        dx, dy = self.direction.value
        return (self.x + dx, self.y + dy)
    
    def copy(self) -> 'Signal':
        """Create a copy of this signal."""
        return Signal(self.x, self.y, self.direction)
    
    def __repr__(self) -> str:
        return f"Signal({self.x}, {self.y}, {self.direction.name})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Signal):
            return False
        return self.x == other.x and self.y == other.y and self.direction == other.direction
