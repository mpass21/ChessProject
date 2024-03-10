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
        self.board = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]
        self.__player = Player.BLACK
        self.__nrows = 8
        self.__ncols = 8
        self.__message_code = None
        self.set_piece(0,0,Rook(self.current_player))
        self.set_piece(0, 1, Knight(self.current_player))
        self.set_piece(0, 2, Bishop(self.current_player))
        self.set_piece(0, 3, Queen(self.current_player))
        self.set_piece(0, 4, King(self.current_player))
        self.set_piece(0, 5, Bishop(self.current_player))
        self.set_piece(0, 6, Knight(self.current_player))
        self.set_piece(0, 7, Rook(self.current_player))
        for i in range(0,8):
            self.set_piece(1, i, Pawn(self.current_player))
        self.set_next_player()
        self.set_piece(7, 0, Rook(self.current_player))
        self.set_piece(7, 1, Knight(self.current_player))
        self.set_piece(7, 2, Bishop(self.current_player))
        self.set_piece(7, 3, Queen(self.current_player))
        self.set_piece(7, 4, King(self.current_player))
        self.set_piece(7, 5, Bishop(self.current_player))
        self.set_piece(7, 6, Knight(self.current_player))
        self.set_piece(7, 7, Rook(self.current_player))
        for i in range(0,8):
            self.set_piece(6, i, Pawn(self.current_player))

    @property
    def nrows(self):
        return self.__nrows

    @property
    def ncols(self):
        return self.__ncols

    @property
    def current_player(self):
        return self.__player

    @property
    def messageCode(self):
        return self.__message_code
        
    def is_complete(self):
        pass
    def is_valid_move(self, move):
        pass
    def move(self, move):
        pass
    def in_check(self, p):
        pass
    def piece_at(self, row: int, col: int):
        return self.board[row][col]
    def set_next_player(self):
        self.__player = Player.next(self.__player)

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        if 0 <= row <= self.__nrows:
            if 0 <= col <= self.__ncols:
                if piece is None or ChessPiece:
                    self.board[row][col] = piece
                else:
                    raise TypeError
            else:
                raise ValueError
        else:
            raise ValueError
    def undo(self):
        pass


    
