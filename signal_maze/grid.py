"""Grid management for the Signal Maze game."""

from typing import Dict, List, Optional, Tuple
from .components import Component, Wire
from .signal import Signal


class Grid:
    """Manages the game grid and components."""
    
    def __init__(self, width: int, height: int):
        """Initialize a grid with specified dimensions."""
        self.width = width
        self.height = height
        self.components: Dict[Tuple[int, int], Component] = {}
        
        # Fill grid with wires by default
        for y in range(height):
            for x in range(width):
                self.components[(x, y)] = Wire(x, y)
    
    def set_component(self, x: int, y: int, component: Component) -> None:
        """Place a component at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.components[(x, y)] = component
    
    def get_component(self, x: int, y: int) -> Optional[Component]:
        """Get component at position (x, y)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.components.get((x, y))
        return None
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Check if position is within grid bounds."""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def get_display_char(self, x: int, y: int, signal_chars: Optional[Dict[Tuple[int, int], str]] = None) -> str:
        """Get display character for position (x, y)."""
        if signal_chars and (x, y) in signal_chars:
            return signal_chars[(x, y)]
        
        component = self.get_component(x, y)
        if component:
            return component.symbol
        return ' '
    
    def display(self, signals: Optional[List[Signal]] = None) -> str:
        """Generate a string representation of the grid."""
        signal_chars = {}
        if signals:
            for signal in signals:
                signal_symbols = {
                    'UP': '↑',
                    'DOWN': '↓',
                    'LEFT': '←',
                    'RIGHT': '→',
                }
                signal_chars[(signal.x, signal.y)] = signal_symbols.get(signal.direction.name, '•')
        
        lines = []
        # Top border
        lines.append('┌' + '─' * self.width + '┐')
        
        # Grid rows
        for y in range(self.height):
            row = '│'
            for x in range(self.width):
                row += self.get_display_char(x, y, signal_chars)
            row += '│'
            lines.append(row)
        
        # Bottom border
        lines.append('└' + '─' * self.width + '┘')
        
        return '\n'.join(lines)
    
    def __repr__(self) -> str:
        return f"Grid({self.width}x{self.height})"
