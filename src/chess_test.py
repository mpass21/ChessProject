import unittest
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from chess_model import ChessModel


class chess_model_test(unittest.TestCase):

    def test_in_check(self):
        pass

    def test_is_valid(self):
        pass

    def test_is_complete(self):
        pass

    def test_move(self):
        pass

    def test_undo(self):
        pass


model = ChessModel
rook = Rook(model.current_player)
queen = Queen(model.current_player)
bishop = Bishop(model.current_player)
knight = Knight(model.current_player)
pawn = Pawn(model.current_player)
king = King(model.current_player)
model.board = [[None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None, None]]


class chess_valid(unittest.TestCase):
    def test_piece(self):
        model.set_piece(model, 4, 3, rook)
        model.set_piece(model, 0, 3, rook)
        move = Move(4, 3, 5, 3)
        self.assertTrue(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 4, 3)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 9, 3)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 4, 9)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(3, 3, 4, 5)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 0, 3)
        self.assertFalse(rook.is_valid_move(move, model.board))

    def test_pawn(self):
        pass

    def test_knight(self):
        pass

    def test_bishop(self):
        pass

    def test_rook(self):
        model.set_piece(model, 4, 3, rook)
        model.set_piece(model, 6, 3, rook)
        move = Move(4, 3, 5, 3)
        self.assertTrue(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 2, 3)
        self.assertTrue(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 4, 0)
        self.assertTrue(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 4, 6)
        self.assertTrue(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 5, 5)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 0, 0)
        self.assertFalse(rook.is_valid_move(move, model.board))
        move = Move(4, 3, 7, 3)
        self.assertFalse(rook.is_valid_move(move, model.board))


    def test_king(self):
        pass

    def test_queen(self):
        pass
