# Signal Maze - Game Mechanics Documentation

## Overview
Signal Maze is a turn-based puzzle game where players guide signals through a grid by manipulating components.

## Core Concepts

### Signals
- Signals are emitted from sources and travel through the grid
- Each signal has a position (x, y) and direction (UP, DOWN, LEFT, RIGHT)
- Signals move one cell per step in their current direction
- Multiple signals can exist simultaneously

### Grid
- Rectangular grid with defined boundaries
- Each cell can contain one component
- Signals that leave the grid boundaries are terminated
- Grid size varies by puzzle level

## Component Types

### 1. Source (^ v < >)
- Emits signals in a fixed direction
- Direction shown by arrow symbol
- Cannot be rotated or toggled
- Starting point for signal flow

### 2. Exit (X)
- Target destination for signals
- Signals terminate when reaching an exit
- All exits must be reached to win
- Cannot be manipulated

### 3. Wire (·)
- Default component, fills empty cells
- Signals pass through unchanged
- Cannot be manipulated

### 4. Mirror (/ \)
- Reflects signals at 90-degree angles
- **CAN BE ROTATED** using 'r' command
- Two orientations:
  - `/` mirror:
    - RIGHT → UP
    - UP → RIGHT
    - LEFT → DOWN
    - DOWN → LEFT
  - `\` mirror:
    - RIGHT → DOWN
    - DOWN → RIGHT
    - LEFT → UP
    - UP → LEFT

### 5. Switch (○ ●)
- Controls signal flow
- **CAN BE TOGGLED** using 't' command
- Two states:
  - `○` (open): Signals pass through
  - `●` (closed): Signals are blocked

### 6. Blocker (█)
- Fixed obstacle
- Always blocks signals
- Cannot be manipulated

### 7. Splitter (+ T)
- Divides signals into multiple directions
- Cannot be manipulated
- Two types:
  - `+` (cross): Splits into all 4 directions (except back)
  - `T` (tee): Splits perpendicular to incoming direction

## Game Flow

### 1. Initialization
- All sources emit signals simultaneously
- Grid state is calculated

### 2. Signal Propagation
```
For each active signal:
  1. Move signal one step in its direction
  2. Check if signal left grid (terminate)
  3. Get component at new position
  4. Apply component's effect:
     - Mirror: Reflect direction
     - Switch: Pass or block
     - Exit: Mark as reached, terminate
     - Splitter: Create new signals
     - Wire: Continue unchanged
  5. Add resulting signals to next step
```

### 3. Loop Detection
- System tracks (x, y, direction) states
- If signal reaches same state twice → infinite loop detected
- Loop signals are terminated automatically
- Prevents game from hanging

### 4. Win Condition
- Game checks if all exits have been reached
- Player wins when ALL exits are reached
- Move counter tracks efficiency

## Player Commands

### Rotate (r)
```
Command: r <x> <y>
Effect: Rotates mirror at position (x, y)
Example: r 4 2
```

### Toggle (t)
```
Command: t <x> <y>
Effect: Toggles switch at position (x, y)
Example: t 7 5
```

### Help (h)
```
Command: h
Effect: Shows help information
```

### Quit (q)
```
Command: q
Effect: Exits the game
```

## Strategy Tips

1. **Trace Signal Paths**: Mentally follow where signals will go before making moves
2. **Work Backwards**: Start from exits and work backwards to sources
3. **Consider Side Effects**: One change affects entire signal flow
4. **Count Moves**: Try to solve puzzles in minimum moves
5. **Use Switches Strategically**: Control which paths are active
6. **Plan Mirror Chains**: Multiple mirrors can create complex paths

## Example Puzzle Solution

### Initial State
```
┌────────┐
│····↑···│
│·→→→↑···│
│········│
│····\·X·│
└────────┘
```
Problem: Signal goes UP, but exit is to the RIGHT

### Solution
```
Command: r 4 1
Rotates mirror from / to \

┌────────┐
│········│
│·→→→↓···│
│····↓···│
│····→→X·│
└────────┘
```
Result: Signal now goes DOWN then RIGHT to reach exit!

## Advanced Concepts

### Signal Splitting
When splitters create multiple signals:
- Each new signal is independent
- All must be tracked separately
- Can create complex multi-path solutions

### Multiple Sources
Puzzles can have multiple sources:
- All sources emit simultaneously
- May need to coordinate paths
- Signals don't interfere with each other

### Timing
Turn-based means:
- All signal flow is recalculated after each move
- Previous signal paths don't persist
- Fresh simulation on every turn

## Technical Details

### Performance
- Loop detection: O(n) where n = unique signal states
- Max steps: 1000 (prevents infinite loops)
- Signal visualization: Shows all signal positions in current turn

### Signal State
Each signal tracks:
- x position (integer)
- y position (integer)
- direction (UP/DOWN/LEFT/RIGHT)

### Component Interaction
Priority order:
1. Check grid boundaries
2. Move signal
3. Get component at new position
4. Process component effect
5. Continue with resulting signals
