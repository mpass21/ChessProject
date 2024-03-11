from abc import ABC, abstractmethod
from player import Player


class ChessPiece(ABC):
    def __init__(self, player: Player):
        self.__player = player

    @property
    def player(self):
        return self.__player

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def is_valid_move(self, move, board):
        if move.from_col > 8 or move.from_col < 0:
            return False
        elif move.from_row > 8 or move.from_row < 0:
            return False
        elif move.to_row > 8 or move.to_row < 0:
            return False
        elif move.to_col > 8 or move.to_col < 0:
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


