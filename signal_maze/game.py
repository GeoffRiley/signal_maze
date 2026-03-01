"""Main game logic for Signal Maze."""

from typing import List, Set, Tuple, Optional
from .grid import Grid
from .components import Component, Source, Exit
from .signal import Signal


class Game:
    """Main game controller for Signal Maze."""
    
    def __init__(self, grid: Grid):
        """Initialize game with a grid."""
        self.grid = grid
        self.sources: List[Source] = []
        self.exits: List[Exit] = []
        self.move_count = 0
        self.max_signal_steps = 1000  # Prevent infinite loops
        
        # Find all sources and exits
        self._scan_special_components()
    
    def _scan_special_components(self) -> None:
        """Scan grid for sources and exits."""
        self.sources = []
        self.exits = []
        
        for component in self.grid.components.values():
            if isinstance(component, Source):
                self.sources.append(component)
            elif isinstance(component, Exit):
                self.exits.append(component)
    
    def simulate_signals(self) -> List[Signal]:
        """Simulate signal flow through the grid."""
        # Reset exit states
        for exit_point in self.exits:
            exit_point.reached = False
        
        # Start with signals from all sources
        active_signals = [source.emit_signal() for source in self.sources]
        all_signals = []
        visited: Set[Tuple[int, int, str]] = set()  # Track (x, y, direction) to detect loops
        
        steps = 0
        while active_signals and steps < self.max_signal_steps:
            steps += 1
            new_signals = []
            
            for signal in active_signals:
                # Record signal position for visualization
                all_signals.append(signal.copy())
                
                # Check for loops
                state = (signal.x, signal.y, signal.direction.name)
                if state in visited:
                    continue  # Skip signals in loops
                visited.add(state)
                
                # Move signal forward
                next_x, next_y = signal.peek_next()
                
                # Check if signal leaves grid
                if not self.grid.is_valid_position(next_x, next_y):
                    continue  # Signal exits grid
                
                signal.move()
                
                # Process signal at new position
                component = self.grid.get_component(signal.x, signal.y)
                if component:
                    resulting_signals = component.process_signal(signal)
                    new_signals.extend(resulting_signals)
            
            active_signals = new_signals
        
        return all_signals
    
    def check_win_condition(self) -> bool:
        """Check if all exits have been reached."""
        if not self.exits:
            return False
        return all(exit_point.reached for exit_point in self.exits)
    
    def rotate_component(self, x: int, y: int) -> bool:
        """Rotate component at position (x, y) if possible."""
        component = self.grid.get_component(x, y)
        if component and component.can_rotate():
            component.rotate()
            self.move_count += 1
            return True
        return False
    
    def toggle_component(self, x: int, y: int) -> bool:
        """Toggle component at position (x, y) if possible."""
        component = self.grid.get_component(x, y)
        if component and component.can_toggle():
            component.toggle()
            self.move_count += 1
            return True
        return False
    
    def get_state(self) -> dict:
        """Get current game state."""
        signals = self.simulate_signals()
        return {
            'grid': self.grid,
            'signals': signals,
            'move_count': self.move_count,
            'won': self.check_win_condition(),
        }
    
    def display(self) -> str:
        """Display current game state."""
        state = self.get_state()
        
        # Show grid with signals
        grid_display = self.grid.display(state['signals'])
        
        # Show status
        status_lines = [
            grid_display,
            f"\nMoves: {self.move_count}",
            f"Exits reached: {sum(1 for e in self.exits if e.reached)}/{len(self.exits)}",
        ]
        
        if state['won']:
            status_lines.append("\n🎉 Congratulations! You solved the puzzle! 🎉")
        
        return '\n'.join(status_lines)
