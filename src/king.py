from chess_piece import ChessPiece


class King(ChessPiece):
    def __str__(self):
        return "king"

    def type(self):
        return 'king'

    def is_valid_move(self, move, board):
        valid = super().is_valid_move(move, board)
        if valid:
            valid = False
        else:
            return valid
        if move.to_row + 1 < 7:
            if board[move.to_row + 1][move.to_col] == board[move.from_row][move.from_col]:
                valid = True
            if move.to_col + 1 < 7:
                if board[move.to_row + 1][move.to_col + 1] == board[move.from_row][move.from_col]:
                    valid = True
                if board[move.to_row][move.to_col + 1] == board[move.from_row][move.from_col]:
                    valid = True
            if move.to_col - 1 > -1:
                if board[move.to_row + 1][move.to_col - 1] == board[move.from_row][move.from_col]:
                    valid = True
                if board[move.to_row][move.to_col - 1] == board[move.from_row][move.from_col]:
                    valid = True
        if move.to_row - 1 > -1:
            if board[move.to_row - 1][move.to_col] == board[move.from_row][move.from_col]:
                valid = True
            if move.to_col + 1 < 7:
                if board[move.to_row - 1][move.to_col + 1] == board[move.from_row][move.from_col]:
                    valid = True
            if move.to_col - 1 > -1:
                if board[move.to_row - 1][move.to_col - 1] == board[move.from_row][move.from_col]:
                    valid = True
        return valid
