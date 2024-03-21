
from chess_piece import ChessPiece
from move import Move
from player import Player

class Queen(ChessPiece):
    """class responsible for the logic behind the queen piece"""
    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        """returns the name of the queen piece when called"""
        return "Queen"

    def type(self):
        """returns the name of the queen piece when called"""
        return "Queen"

    def is_valid_move(self, move: Move, board):
        """method that sees if a given move is possible for the Queen

            parameters:
                move: a move object that represents the desired move for the Queen
                board: a list of lists representation of the chess board that the Queen is on

            returns:
                True: if the move is possible for the Queen
                False: if the move is not possible for the Queen
        """

        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        #checks if queen pases basic piece requirements
        if not super().is_valid_move(move, board):
            return False


        # checking if it is a queen move
        if not (abs(start_row - end_row) == abs(start_col - end_col) or start_col == end_col or start_row == end_row):
            return False
        
        # non-diagonal testing for if there is a piece blocking move
        if start_row == end_row and end_col < start_col:
            for i in range(end_col +1, start_col):
                if board[start_row][i] is not None:
                    return False
        if start_row == end_row and end_col > start_col:
            for i in range(start_col + 1, end_col):
                if board[start_row][i] is not None:
                    return False
        if start_col == end_col and end_row < start_row:
            for i in range(end_row +1, start_row):
                if board[i][start_col] is not None:
                    return False
        if start_col == end_col and end_row > start_row:
            for i in range(start_row + 1, end_row):
                if board[i][start_col] is not None:
                    return False

        # diagonal testing for if there is a piece blocking the move
        if abs(start_row - end_row) == abs(start_col - end_col):
            if end_row > start_row:
                rowChange = 1
            else:
                rowChange = -1
            if end_col > start_col:
                colChange = 1
            else:
                colChange = -1

            rowCount = start_row + rowChange
            colCount = start_col + colChange

            while rowCount != end_row and colCount != end_col:
                if board[rowCount][colCount] is not None:
                    return False
                rowCount += rowChange
                colCount += colChange
        return True





