from chess_piece import ChessPiece


class Knight(ChessPiece):
    def __str__(self):
        return "Knight"

    def type(self):
        return "Knight"

    def is_valid_move(self, move, board):
        pass