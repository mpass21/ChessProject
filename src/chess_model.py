from enum import Enum
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move

class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 2:
            return 'Invalid move.'

        if self.value == 3:
            return 'Invalid -- cannot move into check.'

        if self.value == 4:
            return 'Invalid -- must move out of check.'


class UndoException(Exception):
    pass


class ChessModel:
    def __init__(self):
        self.board = []
        self.__player = None
        self.__nrows = 0
        self.__ncols = 0
        self.__message_code = None
        
    def is_complete(self):
        pass
    def is_valid_move(self, move):
        pass
    def move(self, move):
        pass
    def in_check(self, p):
        pass
    def piece_at(self, row: int, col: int):
        pass
    def set_next_player(self):
        pass
    def set_piece(self, row: int, col: int, piece: ChessPiece):
        pass
    def undo(self):
        pass




    
