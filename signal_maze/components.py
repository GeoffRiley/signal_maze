"""Components for the Signal Maze game."""

from abc import ABC, abstractmethod
from typing import List, Optional
from .signal import Signal, Direction


class Component(ABC):
    """Base class for all grid components."""
    
    def __init__(self, x: int, y: int, symbol: str = '?'):
        """Initialize a component at position (x, y)."""
        self.x = x
        self.y = y
        self.symbol = symbol
    
    @abstractmethod
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Process an incoming signal and return resulting signals."""
        pass
    
    def can_rotate(self) -> bool:
        """Check if this component can be rotated."""
        return False
    
    def rotate(self) -> None:
        """Rotate the component (if supported)."""
        pass
    
    def can_toggle(self) -> bool:
        """Check if this component can be toggled."""
        return False
    
    def toggle(self) -> None:
        """Toggle the component state (if supported)."""
        pass
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Source(Component):
    """Signal source that emits signals in a direction."""
    
    def __init__(self, x: int, y: int, direction: Direction):
        """Initialize a source at position (x, y) emitting in direction."""
        symbols = {
            Direction.UP: '^',
            Direction.DOWN: 'v',
            Direction.LEFT: '<',
            Direction.RIGHT: '>',
        }
        super().__init__(x, y, symbols[direction])
        self.direction = direction
    
    def emit_signal(self) -> Signal:
        """Create a new signal from this source."""
        return Signal(self.x, self.y, self.direction)
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Sources don't process incoming signals."""
        return []


class Exit(Component):
    """Exit point that signals must reach."""
    
    def __init__(self, x: int, y: int, required_direction: Optional[Direction] = None):
        """Initialize an exit at position (x, y)."""
        super().__init__(x, y, 'X')
        self.required_direction = required_direction
        self.reached = False
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Mark exit as reached and terminate signal."""
        if self.required_direction is None or signal.direction == self.required_direction:
            self.reached = True
        return []


class Wire(Component):
    """Wire that allows signals to pass through."""
    
    def __init__(self, x: int, y: int):
        """Initialize a wire at position (x, y)."""
        super().__init__(x, y, '·')
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Allow signal to continue in same direction."""
        return [signal]


class Mirror(Component):
    """Mirror that reflects signals."""
    
    def __init__(self, x: int, y: int, orientation: str = '/'):
        """Initialize a mirror at position (x, y) with orientation '/' or '\\'."""
        super().__init__(x, y, orientation)
        self.orientation = orientation
    
    def can_rotate(self) -> bool:
        return True
    
    def rotate(self) -> None:
        """Toggle mirror orientation between / and \\."""
        if self.orientation == '/':
            self.orientation = '\\'
            self.symbol = '\\'
        else:
            self.orientation = '/'
            self.symbol = '/'
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Reflect signal based on mirror orientation."""
        new_signal = signal.copy()
        
        if self.orientation == '/':
            # / mirror: UP<->RIGHT, DOWN<->LEFT
            reflection = {
                Direction.UP: Direction.RIGHT,
                Direction.RIGHT: Direction.UP,
                Direction.DOWN: Direction.LEFT,
                Direction.LEFT: Direction.DOWN,
            }
        else:  # '\\'
            # \ mirror: UP<->LEFT, DOWN<->RIGHT
            reflection = {
                Direction.UP: Direction.LEFT,
                Direction.LEFT: Direction.UP,
                Direction.DOWN: Direction.RIGHT,
                Direction.RIGHT: Direction.DOWN,
            }
        
        new_signal.direction = reflection[signal.direction]
        return [new_signal]


class Switch(Component):
    """Switch that can be toggled to allow or block signals."""
    
    def __init__(self, x: int, y: int, state: bool = True):
        """Initialize a switch at position (x, y) with initial state."""
        symbol = '○' if state else '●'
        super().__init__(x, y, symbol)
        self.state = state  # True = open (allows signals), False = closed (blocks)
    
    def can_toggle(self) -> bool:
        return True
    
    def toggle(self) -> None:
        """Toggle switch between open and closed."""
        self.state = not self.state
        self.symbol = '○' if self.state else '●'
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Allow signal through if open, block if closed."""
        if self.state:
            return [signal]
        return []


class Blocker(Component):
    """Fixed blocker that always stops signals."""
    
    def __init__(self, x: int, y: int):
        """Initialize a blocker at position (x, y)."""
        super().__init__(x, y, '█')
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Block all signals."""
        return []


class Splitter(Component):
    """Splitter that splits signals in multiple directions."""
    
    def __init__(self, x: int, y: int, split_type: str = '+'):
        """Initialize a splitter at position (x, y) with type + or T."""
        super().__init__(x, y, split_type)
        self.split_type = split_type
    
    def process_signal(self, signal: Signal) -> List[Signal]:
        """Split signal into multiple directions."""
        signals = []
        
        if self.split_type == '+':
            # Split in all 4 directions
            for direction in Direction:
                if direction != signal.direction.opposite():
                    new_signal = signal.copy()
                    new_signal.direction = direction
                    signals.append(new_signal)
        elif self.split_type == 'T':
            # Split perpendicular to incoming direction
            new_signal1 = signal.copy()
            new_signal2 = signal.copy()
            new_signal1.direction = signal.direction.rotate_cw()
            new_signal2.direction = signal.direction.rotate_ccw()
            signals = [new_signal1, new_signal2]
        
        return signals
