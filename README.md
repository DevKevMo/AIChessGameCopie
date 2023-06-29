# Python Chess Game API

This Python Chess Game API allows you to develop chess-related applications and games using Python. It provides a set of classes and functions to handle chess game logic, board representation, move generation, and more.

## Features

- Board representation: Represents the chess board and pieces using a 2D array.
- Move generation: Generates valid moves for each chess piece on the board.
- Game logic: Enforces the rules of chess, including legal moves, check, checkmate, and stalemate conditions.
- PGN support: Supports parsing and generating Portable Game Notation (PGN) files.
- Extensible: Easily integrate the API into your own projects or game applications.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

1. Import the necessary modules:

   ```python
   from chess_game import ChessBoard, ChessPiece, Color, Move