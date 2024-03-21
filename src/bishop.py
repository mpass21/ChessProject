from chess_piece import ChessPiece


class Bishop(ChessPiece):
    """bishop class that controls the logic behind the piece"""

    def __str__(self):
        """returns the string name for the piece if called"""
        return "Bishop"

    def type(self):
        """returns the string name for the piece if called"""
        return 'Bishop'

    def is_valid_move(self, move, board):
        """method that sees if a given move is possible for the bishop

            parameters:
                move: a move object that represents the desired move for the bishop
                board: a list of lists representation of the chess board that the bishop is on

            returns:
                True: if the move is possible for the bishop
                False: if the move is not possible for the bishop
        """
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col
        
        #inherits the basic conditions a chess move has to pass
        if not super().is_valid_move(move, board):
            return False
        
        #checks if the move is diagonal
        if not abs(start_row - end_row) == abs(start_col - end_col):
            return False

        #sets the change values for the diagonal that the bishop is moving on
        if end_row > start_row:
            rowChange = 1
        else:
            rowChange = -1
        if end_col > start_col:
            colChange = 1
        else:
            colChange = -1 
        
        rowCount = start_row + rowChange
        colCount = start_col + colChange

        #checks if there is a piece in the blocking the move 
        while rowCount != end_row and colCount != end_col:
            if board[rowCount][colCount] is not None:
                return False
            rowCount += rowChange
            colCount += colChange
        return True

