# ConnectFiveGame
This is a CLI version of the classic Connect 5 game implemented in Python.

Overview
Connect 5 is a two-player connection game, where the players take turns dropping pieces into a vertically suspended grid. The goal is to form a horizontal, vertical, or diagonal line of five of one's own pieces.

This repository contains a command-line interface for playing Connect 5 against another player locally. It provides an intuitive gameplay experience while ensuring efficient game logic.

Features
Start a new game by specifying the board size
Take turns making moves by entering the column to drop pieces
View the current state of the game board after each move
Detect when a player wins by connecting 5 pieces
Switch between players automatically after each move
Handle invalid moves gracefully
Declare a draw if the board is completely filled
Option to quit the game at any point
Installation
Copy code

pip install -r requirements.txt
Usage
Copy code

python main.py
Follow the prompts to start a new game, make moves, and view the board.

Rules
Connect 5 is played on a rectangular grid of size NxN. Each player takes turns dropping a piece into any of the columns. The piece falls straight down to the lowest available space in that column. The first player to form an unbroken line of 5 pieces horizontally, vertically, or diagonally wins the game.

Documentation
game.py - Contains the main Game class that handles game logic
ui.py - Contains the UI class to manage user interactions
main.py - Entry point to start the CLI application
tests/ - Unit tests for game logic and UI
See comments in source code files for more details.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Let me know if you would like me to modify or expand the README description further. I aimed to provide a high-level overview of the project while calling out key features and implementation details.
