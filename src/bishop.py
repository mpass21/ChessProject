from chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __str__(self):
        return "This is a Bishop"

    def type(self):
        pass

    def is_valid_move(self, move, board):
        valid = ChessPiece.is_valid_move(self, move, board)
        if valid:
            valid = False
        else:
            return valid
        for i in range(1, 7):
            if move.to_row + i < 7:
                if move.to_col + i < 7:
                    if board[move.to_row + i][move.to_col + i] == board[move.from_row][move.from_col]:
                        valid = True
                        break
                if move.to_col - i > -1:
                    if board[move.to_row + i][move.to_col - i] == board[move.from_row][move.from_col]:
                        valid = True
                        break
            if move.to_row - i > -1:
                if move.to_col + i < 7:
                    if board[move.to_row - i][move.to_col + i] == board[move.from_row][move.from_col]:
                        valid = True
                        break
                if move.to_col - 1 > -1:
                    if board[move.to_row - i][move.to_col - i] == board[move.from_row][move.from_col]:
                        valid = True
                        break
        return valid
