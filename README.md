# *Cat-and-Mouse AI Chase**

## Description
**Cat-and-Mouse AI Chase** is a Python game where a cat attempts to catch a mouse on a customizable board with obstacles. Built with Tkinter for the graphical interface, this game features an AI-driven Minimax algorithm with alpha-beta pruning, making for a challenging and strategic experience as you try to outmaneuver the computer-controlled opponent.

## Features
- **Interactive Graphical Interface**: Utilizes Tkinter to provide a user-friendly, interactive experience.
- **Customizable Game Setup**: Allows players to set the board size and number of obstacles, adding replayability and varying difficulty levels.
- **Advanced AI with Minimax Algorithm**: The AI optimally controls the character movements using Minimax with alpha-beta pruning for strategic gameplay.
- **Move Validation**: Ensures all moves are valid and avoid obstacles or board boundaries.
- **Game-End Detection**: The game ends when the cat catches the mouse, with a game-over message displayed.

## How to Play
1. **Configure Game Settings**: Adjust the number of rows, columns, and obstacles from the configuration screen.
2. **Choose Your Character**: Play as either the cat or the mouse.
3. **Control Your Character**: Use the arrow keys to move while the AI controls the other character, calculating moves based on Minimax.
4. **Objective**: As the mouse, avoid the cat; as the cat, try to catch the mouse. The game ends when the cat successfully catches the mouse.
