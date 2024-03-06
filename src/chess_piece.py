from abc import ABC, abstractmethod
from player import Player


class ChessPiece(ABC):
    def __init__(self, player: Player):
        self.__player = player

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def is_valid_move(self, move, board):
        pass
