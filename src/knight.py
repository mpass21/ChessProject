from chess_piece import ChessPiece
from move import Move
from player import Player


class Knight(ChessPiece):
    """
    An abstract class that represents a knight

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        Returns knight for the type of piece
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the move is a valid move for a rook
    """
    def __init__(self, player: Player):
        """
        Constructs the knight piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)

    def __str__(self):
        """returns name of piece"""
        return "Knight"

    def type(self):
        """returns type of piece"""
        return "Knight"

    def is_valid_move(self, move: Move, board):
        """
        Checks if the move is a valid move for a knight

        Parameters
        __________
        move : Move
            a possible move for a knight
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        if not super().is_valid_move(move, board):
            return False

        if end_row == start_row - 2 and abs(start_col - end_col) == 1:
            return True
        if end_row == start_row + 2 and abs(start_col - end_col) == 1:
            return True
        if end_col == start_col + 2 and abs(start_row - end_row) == 1:
            return True
        if end_col == start_col - 2 and abs(start_row - end_row) == 1:
            return True
        return False
