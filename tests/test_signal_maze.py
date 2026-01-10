"""Tests for Signal Maze."""

import pytest
from signal_maze import SignalMaze


class TestSignalMazeInit:
    """Tests for SignalMaze initialization."""

    def test_create_simple_maze(self):
        """Test creating a simple 2x2 maze."""
        grid = [
            ['S', 'X'],
            ['E', 'N']
        ]
        maze = SignalMaze(grid)
        assert maze.rows == 2
        assert maze.cols == 2

    def test_create_empty_maze_raises_error(self):
        """Test that creating an empty maze raises ValueError."""
        with pytest.raises(ValueError, match="Grid cannot be empty"):
            SignalMaze([])

    def test_create_maze_with_empty_rows_raises_error(self):
        """Test that creating a maze with empty rows raises ValueError."""
        with pytest.raises(ValueError, match="Grid cannot be empty"):
            SignalMaze([[]])

    def test_create_maze_with_invalid_signal_raises_error(self):
        """Test that invalid signals raise ValueError."""
        grid = [['N', 'Z', 'X']]
        with pytest.raises(ValueError, match="Invalid signal: Z"):
            SignalMaze(grid)

    def test_create_maze_with_inconsistent_row_lengths_raises_error(self):
        """Test that inconsistent row lengths raise ValueError."""
        grid = [
            ['N', 'S'],
            ['E', 'W', 'X']
        ]
        with pytest.raises(ValueError, match="All rows must have the same length"):
            SignalMaze(grid)


class TestSignalMazeMethods:
    """Tests for SignalMaze methods."""

    def test_is_valid_position(self):
        """Test position validation."""
        grid = [
            ['S', 'E', 'X'],
            ['N', 'E', 'N'],
            ['E', 'N', 'W']
        ]
        maze = SignalMaze(grid)
        
        # Valid positions
        assert maze.is_valid_position(0, 0) is True
        assert maze.is_valid_position(2, 2) is True
        assert maze.is_valid_position(1, 1) is True
        
        # Invalid positions
        assert maze.is_valid_position(-1, 0) is False
        assert maze.is_valid_position(0, -1) is False
        assert maze.is_valid_position(3, 0) is False
        assert maze.is_valid_position(0, 3) is False

    def test_get_signal(self):
        """Test getting signals from positions."""
        grid = [
            ['S', 'E', 'X'],
            ['N', 'W', 'N']
        ]
        maze = SignalMaze(grid)
        
        assert maze.get_signal(0, 0) == 'S'
        assert maze.get_signal(0, 2) == 'X'
        assert maze.get_signal(1, 1) == 'W'
        
        # Invalid positions should return None
        assert maze.get_signal(-1, 0) is None
        assert maze.get_signal(2, 0) is None

    def test_find_exit(self):
        """Test finding the exit position."""
        grid = [
            ['S', 'E', 'N'],
            ['N', 'X', 'N'],
            ['E', 'N', 'W']
        ]
        maze = SignalMaze(grid)
        
        exit_pos = maze.find_exit()
        assert exit_pos == (1, 1)

    def test_find_exit_no_exit(self):
        """Test finding exit when there is no exit."""
        grid = [
            ['S', 'E', 'N'],
            ['N', 'W', 'N']
        ]
        maze = SignalMaze(grid)
        
        exit_pos = maze.find_exit()
        assert exit_pos is None


class TestSignalMazeNavigation:
    """Tests for maze navigation."""

    def test_navigate_simple_path_to_exit(self):
        """Test navigating a simple path to the exit."""
        grid = [
            ['S', 'E', 'X'],
            ['N', 'E', 'N'],
            ['E', 'N', 'W']
        ]
        maze = SignalMaze(grid)
        
        success, path = maze.navigate(0, 0)
        assert success is True
        assert len(path) > 0
        assert path[0] == (0, 0)  # Start position
        # The path should end at the exit
        final_row, final_col = path[-1]
        assert maze.get_signal(final_row, final_col) == 'X'

    def test_navigate_out_of_bounds(self):
        """Test navigation that goes out of bounds."""
        grid = [
            ['N', 'X'],  # 'N' at (0,0) tries to go up, which is out of bounds
            ['E', 'W']
        ]
        maze = SignalMaze(grid)
        
        success, path = maze.navigate(0, 0)
        assert success is False

    def test_navigate_with_cycle(self):
        """Test navigation that encounters a cycle."""
        grid = [
            ['S', 'X'],
            ['N', 'W']  # This creates a cycle between (0,0) and (1,0)
        ]
        maze = SignalMaze(grid)
        
        success, path = maze.navigate(0, 0)
        assert success is False

    def test_navigate_starting_at_exit(self):
        """Test navigation when starting at the exit."""
        grid = [
            ['X', 'E'],
            ['N', 'W']
        ]
        maze = SignalMaze(grid)
        
        success, path = maze.navigate(0, 0)
        assert success is True
        assert path == [(0, 0)]

    def test_navigate_from_different_start(self):
        """Test navigation from a non-default start position."""
        grid = [
            ['N', 'S', 'X'],
            ['E', 'E', 'N'],
            ['N', 'W', 'W']
        ]
        maze = SignalMaze(grid)
        
        success, path = maze.navigate(2, 0)
        assert isinstance(success, bool)
        assert isinstance(path, list)
        if len(path) > 0:
            assert path[0] == (2, 0)


class TestSignalMazeString:
    """Tests for string representation."""

    def test_str_representation(self):
        """Test the string representation of the maze."""
        grid = [
            ['S', 'E', 'X'],
            ['N', 'W', 'N']
        ]
        maze = SignalMaze(grid)
        
        expected = "S E X\nN W N"
        assert str(maze) == expected
