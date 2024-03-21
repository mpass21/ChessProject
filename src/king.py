from chess_piece import ChessPiece
class King(ChessPiece):
    """King class that controls the logic behind the king piece"""
    def __str__(self):
        """returns the name of the king piece when called"""
        return "King"

    def type(self):
        """returns the name of the king piece when called"""
        return 'King'

    def is_valid_move(self, move, board):
        """method that sees if a given move is possible for the king

            parameters:
                move: a move object that represents the desired move for the king
                board: a list of lists representation of the chess board that the king is on

            returns:
                True: if the move is possible for the king
                False: if the move is not possible for the king
        """

        #checks if the king move passes general move requirements for a piece
        valid = super().is_valid_move(move, board)
        if not valid:
            return False
        
        #checks that move is within the range of king moves
        if abs(move.to_col - move.from_col) > 1 or abs(move.to_row - move.from_row) > 1:
            return False
        return True


