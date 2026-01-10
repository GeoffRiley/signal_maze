"""Signal Maze - A turn-based puzzle game with interconnected components."""

__version__ = "0.1.0"

from .game import Game
from .components import Component, Source, Exit, Mirror, Wire, Switch, Blocker, Splitter
from .grid import Grid
from .signal import Signal, Direction

__all__ = [
    "Game",
    "Component",
    "Source",
    "Exit",
    "Mirror",
    "Wire",
    "Switch",
    "Blocker",
    "Splitter",
    "Grid",
    "Signal",
    "Direction",
]
