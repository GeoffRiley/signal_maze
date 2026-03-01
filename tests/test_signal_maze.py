"""Tests for Signal Maze components."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from signal_maze.signal import Signal, Direction
from signal_maze.components import (
    Source, Exit, Wire, Mirror, Switch, Blocker, Splitter
)
from signal_maze.grid import Grid
from signal_maze.game import Game


def test_direction():
    """Test Direction enum."""
    assert Direction.UP.opposite() == Direction.DOWN
    assert Direction.LEFT.opposite() == Direction.RIGHT
    assert Direction.UP.rotate_cw() == Direction.RIGHT
    assert Direction.UP.rotate_ccw() == Direction.LEFT
    print("✓ Direction tests passed")


def test_signal():
    """Test Signal class."""
    sig = Signal(0, 0, Direction.RIGHT)
    assert sig.peek_next() == (1, 0)
    sig.move()
    assert (sig.x, sig.y) == (1, 0)
    
    sig2 = sig.copy()
    assert sig2.x == sig.x and sig2.y == sig.y
    print("✓ Signal tests passed")


def test_mirror():
    """Test Mirror reflection."""
    mirror_forward = Mirror(5, 5, '/')
    mirror_back = Mirror(5, 5, '\\')
    
    # Test / mirror
    sig_right = Signal(5, 5, Direction.RIGHT)
    result = mirror_forward.process_signal(sig_right)
    assert len(result) == 1
    assert result[0].direction == Direction.UP
    
    # Test \ mirror
    sig_right2 = Signal(5, 5, Direction.RIGHT)
    result2 = mirror_back.process_signal(sig_right2)
    assert len(result2) == 1
    assert result2[0].direction == Direction.DOWN
    
    # Test rotation
    mirror_forward.rotate()
    assert mirror_forward.orientation == '\\'
    
    print("✓ Mirror tests passed")


def test_switch():
    """Test Switch toggling."""
    switch = Switch(5, 5, True)
    sig = Signal(5, 5, Direction.RIGHT)
    
    # Open switch allows signals through
    result = switch.process_signal(sig)
    assert len(result) == 1
    
    # Closed switch blocks signals
    switch.toggle()
    assert switch.state == False
    result = switch.process_signal(sig)
    assert len(result) == 0
    
    print("✓ Switch tests passed")


def test_grid():
    """Test Grid functionality."""
    grid = Grid(10, 10)
    
    # Test setting and getting components
    source = Source(0, 0, Direction.RIGHT)
    grid.set_component(0, 0, source)
    assert grid.get_component(0, 0) == source
    
    # Test bounds checking
    assert grid.is_valid_position(0, 0)
    assert grid.is_valid_position(9, 9)
    assert not grid.is_valid_position(10, 10)
    assert not grid.is_valid_position(-1, 0)
    
    print("✓ Grid tests passed")


def test_simple_game():
    """Test a simple game scenario."""
    grid = Grid(10, 5)
    
    # Create a simple path: Source -> Exit
    grid.set_component(0, 2, Source(0, 2, Direction.RIGHT))
    grid.set_component(5, 2, Exit(5, 2))
    
    game = Game(grid)
    
    # Simulate signals
    signals = game.simulate_signals()
    assert len(signals) > 0
    
    # Check if exit was reached
    assert game.check_win_condition()
    print("✓ Simple game test passed")


def test_mirror_game():
    """Test a game with mirrors."""
    grid = Grid(10, 10)
    
    # Source pointing right
    grid.set_component(0, 5, Source(0, 5, Direction.RIGHT))
    
    # Mirror to redirect down
    grid.set_component(5, 5, Mirror(5, 5, '\\'))
    
    # Exit below
    grid.set_component(5, 8, Exit(5, 8))
    
    game = Game(grid)
    
    # Initially won't reach exit (wrong mirror orientation)
    # Need to check signal flow
    signals = game.simulate_signals()
    
    # Check that signals were created
    assert len(signals) > 0
    print("✓ Mirror game test passed")


def test_component_manipulation():
    """Test rotating and toggling components."""
    grid = Grid(5, 5)
    
    # Add rotatable mirror
    mirror = Mirror(2, 2, '/')
    grid.set_component(2, 2, mirror)
    
    # Add toggleable switch
    switch = Switch(3, 3, True)
    grid.set_component(3, 3, switch)
    
    game = Game(grid)
    
    # Test rotation
    assert game.rotate_component(2, 2)
    assert mirror.orientation == '\\'
    assert game.move_count == 1
    
    # Test toggling
    assert game.toggle_component(3, 3)
    assert switch.state == False
    assert game.move_count == 2
    
    # Test invalid operations
    assert not game.rotate_component(0, 0)  # Wire can't rotate
    assert not game.toggle_component(2, 2)  # Mirror can't toggle
    
    print("✓ Component manipulation tests passed")


def test_splitter():
    """Test Splitter component."""
    splitter = Splitter(5, 5, 'T')
    sig = Signal(5, 5, Direction.RIGHT)
    
    # T splitter should split perpendicular
    result = splitter.process_signal(sig)
    assert len(result) == 2
    
    # Check that signals go in perpendicular directions
    directions = {s.direction for s in result}
    assert Direction.UP in directions
    assert Direction.DOWN in directions
    
    print("✓ Splitter tests passed")


def run_all_tests():
    """Run all tests."""
    print("Running Signal Maze tests...\n")
    
    test_direction()
    test_signal()
    test_mirror()
    test_switch()
    test_grid()
    test_simple_game()
    test_mirror_game()
    test_component_manipulation()
    test_splitter()
    
    print("\n✅ All tests passed!")


if __name__ == '__main__':
    run_all_tests()
