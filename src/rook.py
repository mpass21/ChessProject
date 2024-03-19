from chess_piece import ChessPiece
from player import Player

class Rook(ChessPiece):
    """
    An abstract class that represents a rook

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        Returns rook for the type of piece
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the move is a valid move for a rook
    """
    def __init__(self, player: Player):
        """
        Constructs the rook piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)
    def __str__(self):
        """returns name of piece"""
        return "Rook"

    def type(self):
        """returns type of piece"""
        return "Rook"

    def is_valid_move(self, move, board):
        """
        Checks if the move is a valid move for a rook

        Parameters
        __________
        move : Move
            a possible move for a rook
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if abs(move.to_row - move.from_row) > 0 and abs(move.to_col - move.from_col) > 0:
            return False
        if abs(move.to_row - move.from_row) > 0:
            if move.from_row > move.to_row:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if board[move.from_row - i][move.from_col] is not None:
                        return False
            if move.from_row < move.to_row:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if board[move.from_row + i][move.from_col] is not None:
                        return False
        if abs(move.to_col - move.from_col) > 0:
            if move.from_col > move.to_col:
                for i in range(1, abs(move.to_col - move.from_col)):
                    if board[move.from_row][move.from_col - i] is not None:
                        return False
            if move.from_col < move.to_col:
                for i in range(1, abs(move.to_col - move.from_col)):
                    if board[move.from_row][move.from_col + i] is not None:
                        return False
        return True
