from abc import ABC, abstractmethod
from player import Player


class ChessPiece(ABC):
    """
    An abstract class that represents a general chess piece

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        An abstract method for specific chess pieces
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the piece is moving within board, not moving on itself, and not moving into player's own piece
    """
    def __init__(self, player: Player):
        """
        Constructs the chess piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        self.__player = player

    @property
    def player(self):
        """returns player of piece"""
        return self.__player

    @abstractmethod
    def __str__(self):
        """used for specific pieces"""
        pass

    @abstractmethod
    def type(self):
        """used for specific pieces"""
        pass

    @abstractmethod
    def is_valid_move(self, move, board):
        """
        Checks if the move is a valid move on a chessboard

        Parameters
        __________
        move : Move
            a possible move for a chess piece
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        if not (0 <= move.from_row < 8 and 0 <= move.from_col < 8 and 0 <= move.to_row < 8 and 0 <= move.to_col < 8):
            return False
        if move.from_col == move.to_col and move.from_row == move.to_row:
            return False
        if board[move.from_row][move.from_col] != self:
            return False
        if board[move.to_row][move.to_col] is None:
            pass
        elif board[move.to_row][move.to_col].player == self.player:
            return False
        return True


