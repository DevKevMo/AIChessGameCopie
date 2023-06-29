Python Chess Game API
This Python Chess Game API allows you to develop chess-related applications and games using Python. It provides a set of classes and functions to handle chess game logic, board representation, move generation, and more.

Features
Board representation: Represents the chess board and pieces using a 2D array.
Move generation: Generates valid moves for each chess piece on the board.
Game logic: Enforces the rules of chess, including legal moves, check, checkmate, and stalemate conditions.
PGN support: Supports parsing and generating Portable Game Notation (PGN) files.
Extensible: Easily integrate the API into your own projects or game applications.
Installation
Clone the repository or download the source code.
Install the required dependencies by running pip install -r requirements.txt.
Usage
Import the necessary modules:

python
Copy code
from chess_game import ChessBoard, ChessPiece, Color, Move
Create a new chess board:

python
Copy code
board = ChessBoard()
Initialize the board with the starting position:

python
Copy code
board.initialize()
Make moves on the board:

python
Copy code
move = Move((6, 4), (4, 4))  # Move pawn from e7 to e5
board.make_move(move)
Access the board state and pieces:

python
Copy code
current_state = board.get_state()
piece = board.get_piece(4, 4)
Check for game conditions:

python
Copy code
if board.is_checkmate(Color.BLACK):
    print("Checkmate! White wins!")
elif board.is_stalemate(Color.WHITE):
    print("Stalemate! It's a draw!")
Save and load games using PGN files:

python
Copy code
board.save_game("game.pgn")
board.load_game("game.pgn")
For more detailed information on the available classes and methods, refer to the API documentation.

Contributing
Contributions to the Python Chess Game API are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.