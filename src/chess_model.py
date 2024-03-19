from enum import Enum
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move
import copy

class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 2:
            return 'Invalid move.'

        if self.value == 3:
            return 'Invalid -- cannot move into check.'

        if self.value == 4:
            return 'Invalid -- must move out of check.'


class UndoException(Exception):
    pass


class ChessModel:
    def __init__(self):
  
        self.board = [[None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None]]
        self.moveList = []
        self.__player = Player.BLACK
        self.__nrows = 8
        self.__ncols = 8
        self.__message_code = None
        self.set_piece(0, 0, Rook(self.current_player))
        self.set_piece(0, 1, Knight(self.current_player))
        self.set_piece(0, 2, Bishop(self.current_player))
        self.set_piece(0, 3, Queen(self.current_player))
        self.set_piece(0, 4, King(self.current_player))
        self.set_piece(0, 5, Bishop(self.current_player))
        self.set_piece(0, 6, Knight(self.current_player))
        self.set_piece(0, 7, Rook(self.current_player))
        for i in range(0, 8):
            self.set_piece(1, i, Pawn(self.current_player))
        self.set_next_player()
        self.set_piece(7, 0, Rook(self.current_player))
        self.set_piece(7, 1, Knight(self.current_player))
        self.set_piece(7, 2, Bishop(self.current_player))
        self.set_piece(7, 3, Queen(self.current_player))
        self.set_piece(7, 4, King(self.current_player))
        self.set_piece(7, 5, Bishop(self.current_player))
        self.set_piece(7, 6, Knight(self.current_player))
        self.set_piece(7, 7, Rook(self.current_player))
        for i in range(0, 8):
            self.set_piece(6, i, Pawn(self.current_player))
        self.updateMoveList(self.board)

    @property
    def nrows(self):
        return self.__nrows

    @property
    def ncols(self):
        return self.__ncols

    @property
    def current_player(self):
        return self.__player

    @property
    def messageCode(self):
        return self.__message_code

    def is_complete(self):
        piece_lst = [Queen, Rook, Bishop, Knight, Pawn, King]
        for i in range(0, 8):
            for j in range(0, 8):
                for piece in piece_lst:
                    if isinstance(self.piece_at(i, j), piece):
                        if self.piece_at(i, j).player == self.current_player:
                            for x in range(0, 8):
                                for y in range(0, 8):
                                    move = Move(i,j,x,y)
                                    if self.piece_at(i, j).is_valid_move(move, self.board):
                                        testBoard = self.copy_board(self.board)
                                        self.move_piece_test(testBoard, move)
                                        if not self.in_check_pt2(self.current_player, testBoard):
                                            return False
   
        return True
    def is_valid_move(self, move):
        start_row, start_col = move.from_row, move.from_col
        piece = self.board[start_row][start_col]
        if not piece:   
            return False
        
        testBoard = self.copy_board(self.board)
        self.move_piece_test(testBoard, move)
        if self.in_check_pt2(self.current_player,testBoard):
            return False

        return piece.is_valid_move(move, self.board)

    def move_piece_test(self, board, move):
        piece = board[move.from_row][move.from_col]
        board[move.to_row][move.to_col] = piece
        board[move.from_row][move.from_col] = None
    
    def in_check_pt2(self,player,board):
        kingRow = None
        kingCol = None
        for row in range(8):
            for col in range(8):
                if isinstance(board[row][col], King) and board[row][col].player == player:
                    kingRow = row
                    kingCol = col
                    break

        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for row, col in knight_moves:
            attack_row, attack_col = kingRow + row, kingCol + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], Knight) and board[attack_row][attack_col].player != player:
                    return True
                
        king_moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for row, col in king_moves:
            attack_row, attack_col = kingRow + row, kingCol + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], King) and board[attack_row][attack_col].player != player:
                    return True


        if player== Player.WHITE:
            pawn_moves = (-1, -1), (-1, 1)
        else:
            pawn_moves = (1, 1), (1, -1)

        for row, col in pawn_moves:
            attack_row, attack_col = kingRow + row, kingCol + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], Pawn) and board[attack_row][attack_col].player != player:
                    return True

     
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diagonal_directions:
            for i in range(1, 8):
                new_row, new_col = kingRow + i * dr, kingCol + i * dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col]:
                        if board[new_row][new_col].player == player:
                            break
                        elif isinstance(board[new_row][new_col], (Bishop, Queen)):
                            return True
                        else:
                            break
                else:
                    break

      
        horizontal_vertical_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in horizontal_vertical_directions:
            for i in range(1, 8):
                new_row, new_col = kingRow + i * dr, kingCol + i * dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col]:
                        if board[new_row][new_col].player == player:
                            break
                        elif isinstance(board[new_row][new_col], (Rook, Queen)):
                            return True
                        else:
                            break
                else:
                    break

        return False
            
    def updateMoveList(self,board):
        copied_board = self.copy_board(board)
        self.moveList.append(copied_board)

    def move(self, move):
        if str(self.piece_at(move.from_row, move.from_col)) == 'Pawn' and (move.to_row == 0 or move.to_row == 7):
            self.set_piece(move.to_row, move.to_col, Queen(self.current_player))
        else:
            self.set_piece(move.to_row, move.to_col, self.piece_at(move.from_row, move.from_col))
        self.board[move.from_row][move.from_col] = None
        self.updateMoveList(self.board)
        self.set_next_player()

    def in_check(self, p):
        a = 0
        b = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if isinstance(self.piece_at(i, j), King) and self.piece_at(i, j).player == p:
                    a = i
                    b = j
                    break
        if (a + 2) < 8:
            if b + 1 < 8:
                if isinstance(self.piece_at(a+2, b+1), Knight):
                    if self.piece_at(a + 2, b + 1).player != p:
                        return True
            if b - 1 >= 0:
                if isinstance(self.piece_at(a+2, b-1), Knight):
                    if self.piece_at(a + 2, b - 1).player != p:
                        return True
        if (a - 2) >= 0:
            if b + 1 < 8:
                if isinstance(self.piece_at(a-2, b+1), Knight):
                    if self.piece_at(a - 2, b + 1).player != p:
                        return True
            if b - 1 >= 0:
                if isinstance(self.piece_at(a+2, b-1), Knight):
                    if self.piece_at(a + 2, b - 1).player != p:
                        return True
        if (b + 2) < 8:
            if a + 1 < 8:
                if isinstance(self.piece_at(a+1, b+2), Knight):
                    if self.piece_at(a + 1, b + 2).player != p:
                        return True
            if a - 1 >= 0:
                if isinstance(self.piece_at(a-1, b+2), Knight):
                    if self.piece_at(a - 1, b + 2).player != p:
                        return True
        if (b - 2) >= 0:
            if a + 1 < 8:
                if isinstance(self.piece_at(a+1, b-2), Knight):
                    if self.piece_at(a + 1, b - 2).player != p:
                        return True
            if a - 1 >= 0:
                if isinstance(self.piece_at(a-1, b-2), Knight):
                    if self.piece_at(a - 1, b - 2).player != p:
                        return True

        if a - 1 >= 0:
            if b + 1 < 8:
                if isinstance(self.piece_at(a-1, b+1), Pawn):
                    if self.piece_at(a - 1, b + 1).player != p:
                        return True
            if b - 1 >= 0:
                if isinstance(self.piece_at(a-1, b-1), Pawn):
                    if self.piece_at(a - 1, b - 1).player != p:
                        return True
        if a + 1 < 8:
            if b + 1 < 8:
                if isinstance(self.piece_at(a+1, b+1), Pawn):
                    if self.piece_at(a + 1, b + 1).player != p:
                        return True
            if b - 1 >= 0:
                if isinstance(self.piece_at(a+1, b-1), Pawn):
                    if self.piece_at(a + 1, b - 1).player != p:
                        return True
                    

        for i in range(1, 8):
            if a + i < 8:
                if isinstance(self.piece_at(a+i, b), Rook) or isinstance(self.piece_at(a+i, b), Queen):
                    if self.piece_at(a + i, b).player != p:
                        for j in range(1, i+1):
                            if isinstance(self.piece_at((a+i)-j, b), King):
                                return True
                            if self.piece_at((a+i)-j, b) is not None:
                                break
                if b + i < 8:
                    if isinstance(self.piece_at(a + i, b+i), Bishop) or isinstance(self.piece_at(a + i, b+i), Queen):
                        if self.piece_at(a + i, b+i).player != p:
                            for j in range(1, i + 1):
                                if isinstance(self.piece_at((a+i) - j, (b+i) - j), King):
                                    return True
                                if self.piece_at((a+i) - j, (b+i) - j) is not None:
                                    break
                if b - i >= 0:
                    if isinstance(self.piece_at(a + i, b-i), Bishop) or isinstance(self.piece_at(a + i, b-i), Queen):
                        if self.piece_at(a + i, b-i).player != p:
                            for j in range(1, i + 1):
                                if isinstance(self.piece_at((a+i) - j, (b-i) + j), King):
                                    return True
                                if self.piece_at((a+i) - j, (b-i) + j) is not None:
                                    break
            if a - i >= 0:
                if isinstance(self.piece_at(a - i, b), Rook) or isinstance(self.piece_at(a - i, b), Queen):
                    if self.piece_at(a - i, b).player != p:
                        for j in range(1, i+1):
                            if isinstance(self.piece_at((a-i)+j, b), King):
                                return True
                            if self.piece_at((a-i)+j, b) is not None:
                                break
                if b + i < 8:
                    if isinstance(self.piece_at(a - i, b+i), Bishop) or isinstance(self.piece_at(a - i, b+i), Queen):
                        if self.piece_at(a - i, b+i).player != p:
                            for j in range(1, i + 1):
                                if isinstance(self.piece_at((a-i) + j, (b+i) - j), King):
                                    return True
                                if self.piece_at((a-i) + j, (b+i) - j) is not None:
                                    break
                if b - i >= 0:
                    if isinstance(self.piece_at(a - i, b-i), Bishop) or isinstance(self.piece_at(a - i, b-i), Queen):
                        if self.piece_at(a - i, b-i).player != p:
                            for j in range(1, i + 1):
                                if isinstance(self.piece_at((a-i) + j, (b-i) + j), King):
                                    return True
                                if self.piece_at((a-i) + j, (b-i) + j) is not None:
                                    break
            if b + i < 8:
                if isinstance(self.piece_at(a, b+i), Rook) or isinstance(self.piece_at(a, b+i), Queen):
                    if self.piece_at(a, b+i).player != p:
                        for j in range(1, i+1):
                            if isinstance(self.piece_at(a, (b+i)-j), King):
                                return True
                            if self.piece_at(a, (b+i)-j) is not None:
                                break
            if b - i >= 0:
                if isinstance(self.piece_at(a, b-i), Rook) or isinstance(self.piece_at(a, b-i), Queen):
                    if self.piece_at(a, b-i).player != p:
                        for j in range(1, i+1):
                            if isinstance(self.piece_at(a, (b-i)+j), King):
                                return True
                            if self.piece_at(a, (b-i)+j) is not None:
                                break
        return False

                
    def piece_at(self, row: int, col: int):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]

    def set_next_player(self):
        self.__player = Player.next(self.__player)

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        if 0 <= row < self.__nrows:
            if 0 <= col < self.__ncols:
                if piece is None or ChessPiece:
                    self.board[row][col] = piece
                else:
                    raise TypeError
            else:
                raise ValueError
        else:
            raise ValueError
    def copy_board(self, board):
        newBoard = []
        for row in board:
            newBoard.append(copy.copy(row))
        return newBoard
    

    def undo(self):
        if len(self.moveList) > 1:
            self.moveList.pop()  
            self.board = self.copy_board(self.moveList[-1])
            self.set_next_player()
        else:
            raise UndoException("No moves left to undo")
