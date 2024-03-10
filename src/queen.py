from chess_piece import ChessPiece


class Queen(ChessPiece):
    def __str__(self):
        return "Queen"

    def type(self):
        return "Queen"

    def is_valid_move(self, move, board):
        pass