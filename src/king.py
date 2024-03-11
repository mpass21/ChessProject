from chess_piece import ChessPiece


class King(ChessPiece):
    def __str__(self):
        return "King"

    def type(self):
        return 'King'

    def is_valid_move(self, move, board):
        valid = super().is_valid_move(move, board)
        if valid:
            valid = False
        else:
            return valid
        if abs(move.to_col - move.from_col) > 1 or abs(move.to_row - move.from_row) > 1:
            return False
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
