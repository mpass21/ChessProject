from chess_piece import ChessPiece


class Rook(ChessPiece):
    """"class responsible for the logic behind the rook piece"""
    def __str__(self):
        """returns the name of the rook piece"""
        return "Rook"
        
    def type(self):
        """returns the name of the rook piece"""
        return "Rook"

    def is_valid_move(self, move, board):
        """method that sees if a given move is possible for the rook

            parameters:
                move: a move object that represents the desired move for the rook
                board: a list of lists representation of the chess board that the rook is on

            returns:
                True: if the move is possible for the rook
                False: if the move is not possible for the rook
        """

        #makes sure move pases basic move tests
        valid = super().is_valid_move(move, board)
        if not valid:
            return False
        

        if abs(move.to_row - move.from_row) > 0 and abs(move.to_col - move.from_col) > 0:
            return False
        
        #checks if valid rook move by seeing if there is a piece blocking the move
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
