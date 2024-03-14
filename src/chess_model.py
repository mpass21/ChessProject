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
    def __str__(self):
        return 'No moves left to undo'


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
        self.__message_code = MoveValidity
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
        if self.in_check(self.current_player):
            a = 0
            b = 0
            piece_lst = [Queen,Rook,Bishop,Knight,Pawn]
            for i in range(0, 8):
                for j in range(0, 8):
                    if isinstance(self.piece_at(i, j), King):
                        if self.piece_at(i, j).player == self.current_player:
                            a = i
                            b = j
                            break
            move_u = Move(a, b, a+1, b)
            move_d = Move(a, b, a-1, b)
            move_l = Move(a, b, a, b-1)
            move_r = Move(a, b, a, b+1)
            move_u_r = Move(a, b, a-1, b+1)
            move_u_l = Move(a, b, a-1, b-1)
            move_d_r = Move(a, b, a+1, b+1)
            move_d_l = Move(a, b, a+1, b-1)
            move_lst = [move_u,move_d,move_l,move_r,move_u_r,move_u_l,move_d_l,move_d_r]
            for move in move_lst:
                if self.piece_at(a, b).is_valid_move(move, self.board):
                    self.move(move)
                    self.set_next_player()
                    if not self.in_check(self.current_player):
                        self.undo()
                        self.set_next_player()
                        return False
                    self.undo()
                    self.set_next_player()
            for i in range(0, 8):
                for j in range(0, 8):
                    for piece in piece_lst:
                        if isinstance(self.piece_at(i, j), piece):
                            if self.piece_at(i, j).player == self.current_player:
                                for x in range(0, 8):
                                    for y in range(0, 8):
                                        move = Move(i,j,x,y)
                                        if self.piece_at(i, j).is_valid_move(move, self.board):
                                            self.move(move)
                                            self.set_next_player()
                                            if not self.in_check(self.current_player):
                                                self.undo()
                                                self.set_next_player()
                                                return False
                                            self.undo()
                                            self.set_next_player()
            return True
        else:
            return False

    def is_valid_move(self, move):
        start_row, start_col = move.from_row, move.from_col
        piece = self.board[start_row][start_col]
        if not piece:
            return False
        x = piece.is_valid_move(move, self.board)
        self.move(move)
        self.set_next_player()
        if self.in_check(self.current_player):
            x = False
        self.undo()
        self.set_next_player()
        return x

    def copy_board(self, board):
        newBoard = []
        for row in board:
            newBoard.append(copy.copy(row))
        return newBoard

    def updateMoveList(self, board):
        copied_board = self.copy_board(board)
        self.moveList.append(copied_board)

    def move(self, move):
        if isinstance(self.piece_at(move.from_row, move.from_col), Pawn) and (move.to_row == 0 or move.to_row == 7):
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
                if isinstance(self.piece_at(i, j), King):
                    if self.piece_at(i, j).player == p:
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
        self.board[row][col] = piece

    def undo(self):
        if len(self.moveList) > 1:
            self.moveList.pop()
            self.board = self.copy_board(self.moveList[-1])
            self.set_next_player()
        else:
            raise UndoException("No moves left to undo")