from chess_piece import ChessPiece
from move import Move
from player import Player


class Pawn(ChessPiece):
    """
    An abstract class that represents a pawn

    Attributes
    ___________
    player: Player
        The type of player the piece is

    Methods
    _______
    player:
        Returns the player of the piece
    type:
        Returns pawn for the type of piece
    is_valid_move(move: Move, board, lst[lst[]]):
        Checks if the move is a valid move for a pawn
    """
    def __init__(self, player: Player):
        """
        Constructs the pawn piece

        Parameters
        __________
        player : Player
            the player of the chess piece
        """
        super().__init__(player)

    def __str__(self):
        """returns name of piece"""
        return "Pawn"

    def type(self):
        """returns type of piece"""
        return "Pawn"

    def is_valid_move(self, move: Move, board):
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        # Setting the variables based on color
        if self.player == Player.WHITE:
            direction = -1
            begin_row = 6
        else:
            direction = 1
            begin_row = 1

        if move.from_col == move.to_col and move.from_row == move.to_row:
            return False
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        if board[start_row][start_col].player != self.player:
            return False
        if board[start_row][start_col] != self:
            return False

        if start_col == end_col and end_row == start_row + direction and board[end_row][end_col] is None:
            return True
        if start_row == begin_row and start_col == end_col and end_row == start_row + direction * 2:
            if board[end_row][end_col] is None and board[end_row - direction][end_col] is None:
                return True
        if abs(start_col - end_col) == 1 and end_row == start_row + direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].player != self.player:
                return True
        return False













