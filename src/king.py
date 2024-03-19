from chess_piece import ChessPiece
from player import Player
class King(ChessPiece):
    """
    An abstract class that represents a king

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        Returns king for the type of piece
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the move is a valid move for a king
    """
    def __init__(self, player: Player):
        """
        Constructs the king piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)
    def __str__(self):
        """returns name of piece"""
        return "King"

    def type(self):
        """returns type of piece"""
        return 'King'

    def is_valid_move(self, move, board):
        """
        Checks if the move is a valid move for a king

        Parameters
        __________
        move : Move
            a possible move for a king
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if abs(move.to_col - move.from_col) > 1 or abs(move.to_row - move.from_row) > 1:
            return False
        return True


