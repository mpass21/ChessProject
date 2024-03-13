from chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __str__(self):
        return "Bishop"

    def type(self):
        return 'Bishop'

    def is_valid_move(self, move, board):
        valid = super().is_valid_move(move, board)
        if valid:
            pass
        else:
            return False
        if not (abs(move.to_row - move.from_row) > 0 and abs(move.to_col - move.from_col) > 0):
            return False
        if move.to_row - move.from_row > 0:
            if move.to_col - move.from_col > 0:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row + i < 8 and move.from_col + i < 8:
                        if board[move.from_row + i][move.from_col + i] is not None:
                            return False
            else:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_col - i >= 0 and move.from_row + i < 8:
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
        else:
            if move.to_col - move.from_col > 0:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row - i >= 0 and move.from_col + i < 8:
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
            else:
                for i in range(1, abs(move.to_row - move.from_row)):
                    if move.from_row - i >= 0 and move.from_col - i >= 0:
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
        return True
