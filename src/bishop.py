from chess_piece import ChessPiece
from player import Player

class Bishop(ChessPiece):
    """
    An abstract class that represents a bishop

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        Returns bishop for the type of piece
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the move is a valid move for a bishop
    """
    def __init__(self, player: Player):
        """
        Constructs the bishop piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)
    def __str__(self):
        """returns name of piece"""
        return "Bishop"

    def type(self):
        """returns type of piece"""
        return 'Bishop'

    def is_valid_move(self, move, board):
        """
        Checks if the move is a valid move for a bishop

        Parameters
        __________
        move : Move
            a possible move for a bishop
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if not (abs(move.to_row - move.from_row) == abs(move.to_col - move.from_col)):
            return False
        if move.to_row - move.from_row > 0:
            if move.to_col - move.from_col > 0:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row + i < 8 and move.from_col + i < 8:
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
            else:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_col - i >= 0 and move.from_row + i < 8:
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
        else:
            if move.to_col - move.from_col > 0:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row - i >= 0 and move.from_col + i < 8:
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
            else:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row - i >= 0 and move.from_col - i >= 0:
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
        return True
