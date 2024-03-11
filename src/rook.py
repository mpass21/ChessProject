from chess_piece import ChessPiece


class Rook(ChessPiece):
    def __str__(self):
        return "Rook"

    def type(self):
        return "Rook"

    def is_valid_move(self, move, board):
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if abs(move.to_row - move.from_row) > 0 and abs(move.to_col - move.from_col) > 0:
            return False
        if abs(move.to_row - move.from_row) > 0:
            if move.from_row > move.to_row:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if board[move.from_row - i][move.from_col] is not None:
                        return False
            if move.from_row < move.to_row:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if board[move.from_row + i][move.from_col] is not None:
                        return False
        if abs(move.to_col - move.from_col) > 0:
            if move.from_col > move.to_col:
                for i in range(1, abs(move.to_col - move.from_col)):
                    if board[move.from_row][move.from_col - i] is not None:
                        return False
            if move.from_col < move.to_col:
                for i in range(1, abs(move.to_col - move.from_col)):
                    if board[move.from_row][move.from_col + i] is not None:
                        return False
        return True
