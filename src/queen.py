from chess_piece import ChessPiece
from move import Move
from player import Player


class Queen(ChessPiece):
    """
        An abstract class that represents a queen

        Attributes
        ___________
        player: Player
            The type of player the piece is

        Methods
        _______
        player:
            Returns the player of the piece
        type:
            Returns queen for the type of piece
        is_valid_move(move: Move, board, lst[lst[]]):
            Checks if the move is a valid move for a queen
        """

    def __init__(self, player: Player):
        """
        Constructs the queen piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)

    def __str__(self):
        """returns name of piece"""
        return "Queen"

    def type(self):
        """returns type of piece"""
        return "Queen"

    def is_valid_move(self, move: Move, board):
        """
        Checks if the move is a valid move for a queen

        Parameters
        __________
        move : Move
            a possible move for a queen
        board : lst[lst[]]
            a list of lists that represents a chessboard
        """
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        if not super().is_valid_move(move, board):
            return False

        # checking if it is a queen move
        if not (abs(start_row - end_row) == abs(start_col - end_col) or start_col == end_col or start_row == end_row):
            return False
        # non-diagonal
        if start_row == end_row and end_col < start_col:
            for i in range(end_col + 1, start_col):
                if board[start_row][i] is not None:
                    return False
        if start_row == end_row and end_col > start_col:
            for i in range(start_col + 1, end_col):
                if board[start_row][i] is not None:
                    return False
        if start_col == end_col and end_row < start_row:
            for i in range(end_row + 1, start_row):
                if board[i][start_col] is not None:
                    return False
        if start_col == end_col and end_row > start_row:
            for i in range(start_row + 1, end_row):
                if board[i][start_col] is not None:
                    return False

        # diagonal conditions
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
