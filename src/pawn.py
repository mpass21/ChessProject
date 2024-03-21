
from chess_piece import ChessPiece
from move import Move
from player import Player


class Pawn(ChessPiece):
    """class responsible for the logic behind the pawn piece"""
    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        """returns the name of the pawn piece"""
        return "Pawn"

    def type(self):
        """returns the name of the pawn piece"""
        return "Pawn"

    def is_valid_move(self, move: Move, board):
        """method that sees if a given move is possible for the pawn

            parameters:
                move: a move object that represents the desired move for the pawn
                board: a list of lists representation of the chess board that the pawn is on

            returns:
                True: if the move is possible for the pawn
                False: if the move is not possible for the pawn
        """

        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        # Setting the variables based on color
        if self.player == Player.WHITE:
            direction = -1
            begin_row = 6
        else:
            direction = 1
            begin_row = 1

        #inheriting the basic chess piece tests 
        if not super().is_valid_move(move, board):
            return False

        #checking if move is possible for the pawn
        if start_col == end_col and end_row == start_row + direction and board[end_row][end_col] is None:
            return True
        
        #checking if the move is a double move from the starting row
        if start_row == begin_row and start_col == end_col and end_row == start_row + direction * 2:
            if board[end_row][end_col] is None and board[end_row - direction][end_col] is None:
                return True
            
        #checking if the move is a basic pawn move
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].player != self.player:
                return True
        return False













