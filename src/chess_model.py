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
        self.__player = None
        self.__nrows = 8
        self.__ncols = 8
        self.board = self.createBoard(self.__nrows, self.__ncols)


    def createBoard(self, rows, cols):
        board = [] 
        for _ in range(rows):
            row = [None] * cols
            board.append(row)
        return board
    def printBoard(self):
        for row in self.board:
            print(row)
    def getBoard(self):
        return self.board
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
        self.board[row][col] = "YYYY"
    def undo(self):
        pass




joe = Player(1)
pawn = Pawn(joe)
model = ChessModel()

model.printBoard()
print("test")
start = 1
end = 2

for i in range(start+1, end):
    print(i)
    model.set_piece(3,i,pawn)
model.printBoard()







    
