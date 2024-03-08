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
        valid = True
        if move.from_col > 7 or move.from_col < -1:
            valid = False
        elif move.from_row > 7 or move.from_row < -1:
            valid = False
        elif move.to_row > 7 or move.to_row < -1:
            valid = False
        elif move.to_col > 7 or move.to_col < -1:
            valid = False
        if move.from_col == move.to_col and move.from_row == move.to_row:
            valid = False
        if board[move.from_row][move.from_col] != self:
            valid = False
        if board[move.to_row][move.to_col].player == self.player:
            valid = False
        return valid
