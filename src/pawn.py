from chess_piece import ChessPiece
from move import Move
from player import Player



class Pawn(ChessPiece):
    def __init__(self, player):
        self.__player = player

    def __str__(self):
        return "pawn"

    def type(self):
        return "pawn"

    def is_valid_move(self, move, board):
        #y is row and x is column
        #starting locations are row 6,0-7
        start_row, start_col = move.start_row, move.start_col
        end_row, end_col = move.end_row, move.end_col


        #setting the varibles based on color
        if self.__player == Player.White:
            beginCol = 6
            degree = 1
        else:
            beginCol = 1
            degree -1
        

        #for moving forward one move 
        if start_col == end_col and end_row == start_row + degree:
            if board[end_row][end_col] is None:
                return True
            return False

        #for starting move of white 
        if start_row == beginCol and start_col >= 0 and start_col < 8 and end_col == start_col and end_row == start_row + degree*2:
            if board[end_row][end_col] is None and board[end_row][end_col-1] is None:
                return True
            return False

        
        #for capturing as white
        if ((end_col == start_col - 1) or (end_col == start_col + 1)) and end_row == start_row + degree:
            if board[end_row][end_col]:
                return True
            return False
        

testFirstRow = 3
testLastRow = 4
testfirstCol = 2
testLastCol = 4

#joe = Player(1)
#dog = Pawn(joe)
#move = Move(testFirstRow, testfirstCol, testLastRow, testLastCol)


#dog.is_valid_move(move,)
