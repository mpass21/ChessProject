from chess_piece import ChessPiece


class Bishop(ChessPiece):
    def __str__(self):
        return "Bishop"

    def type(self):
        return 'Bishop'

    def is_valid_move(self, move, board):
    
        start_row, start_col = move.from_row, move.from_col
        end_row, end_col = move.to_row, move.to_col
        
        if not super().is_valid_move(move, board):
            return False
        
        if not abs(start_row - end_row) == abs(start_col - end_col):
            return False


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

        while rowCount != end_row and colCount != end_col:
            if board[rowCount][colCount] is not None:
                return False
            rowCount += rowChange
            colCount += colChange
        return True

