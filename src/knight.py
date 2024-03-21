from chess_piece import ChessPiece
from move import Move
from player import Player


class Knight(ChessPiece):
    """controls the movement logic for the knight piece"""
    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        """returns the name of the knight piece when called"""
        return "Knight"

    def type(self):
        """returns the name of the knight piece when called"""
        return "Knight"

    def is_valid_move(self, move: Move, board):     
        """method that sees if a given move is possible for the knight

            parameters:
                move: a move object that represents the desired move for the knight
                board: a list of lists representation of the chess board that the knight is on

            returns:
                True: if the move is possible for the knight
                False: if the move is not possible for the knight
        """
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col
    
        #test if the knight move passes the basic move requirements for chesspiece
        if not super().is_valid_move(move, board):
            return False

        #tests if the move is within the possible knight moves
        if end_row == start_row - 2 and abs(start_col - end_col) == 1:
            return True
        if end_row == start_row + 2 and abs(start_col - end_col) == 1:
            return True
        if end_col == start_col + 2 and abs(start_row - end_row) == 1:
            return True
        if end_col == start_col - 2 and abs(start_row - end_row) == 1:
            return True
        return False