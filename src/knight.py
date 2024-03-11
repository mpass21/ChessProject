from chess_piece import ChessPiece
from move import Move
from player import Player

class Knight(ChessPiece):
    def __init__(self, player: Player):
        super().__init__(player)

    def __str__(self):
        return "knight"

    def type(self):
        return "knight"

    def is_valid_move(self, move: Move, board):
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col

        if start_col == end_col and start_row == end_row:
            return False
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False
        if board[start_row][start_col].player !=self.player:
            return False
        if board[start_row][start_col] != self:
            return False
        
        if board[end_row][end_col] is not None and board[end_row][end_col].player == self.player:
            return False

        
        if end_row == start_row - 2 and abs(start_col - end_col) == 1:
            return True
        if end_row == start_row + 2 and abs(start_col - end_col) == 1:
            return True
        if end_col == start_col + 2 and abs(start_row - end_row) == 1:
            return True
        if end_col == start_col - 2 and abs(start_row - end_row) == 1:
            return True
        return False
