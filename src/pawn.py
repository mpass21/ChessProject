from chess_piece import ChessPiece


class Pawn(ChessPiece):
    def __str__(self):
        return "Pawn"

    def type(self):
        return "Pawn"

    def is_valid_move(self, move, board):
        pass