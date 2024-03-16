from chess_piece import ChessPiece
from player import Player
class King(ChessPiece):
    def __init__(self, player: Player):
        super().__init__(player)
    def __str__(self):
        return "King"

    def type(self):
        return 'King'

    def is_valid_move(self, move, board):
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if abs(move.to_col - move.from_col) > 1 or abs(move.to_row - move.from_row) > 1:
            return False
        return True


