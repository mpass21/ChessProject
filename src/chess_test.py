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


def clear():
    return [[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]



class chess_model_test(unittest.TestCase):

    def test_in_check(self):
        pass

    def test_is_valid(self):
        pass

    def test_is_complete(self):
        com_model = ChessModel()
        rook_w = Rook(com_model.current_player)
        queen_w = Queen(com_model.current_player)
        bishop_w = Bishop(com_model.current_player)
        knight_w = Knight(com_model.current_player)
        pawn_w = Pawn(com_model.current_player)
        king_w = King(com_model.current_player)
        com_model.set_next_player()
        rook_b = Rook(com_model.current_player)
        queen_b = Queen(com_model.current_player)
        bishop_b = Bishop(com_model.current_player)
        knight_b = Knight(com_model.current_player)
        pawn_b = Pawn(com_model.current_player)
        king_b = King(com_model.current_player)
        com_model.set_next_player()
        com_model.board = clear()
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(0, 0, bishop_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(0, 2, rook_w)
        com_model.set_piece(3, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(0, 0, bishop_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(0, 2, rook_w)
        com_model.set_piece(1, 4, rook_w)
        com_model.set_piece(1, 2, rook_w)
        com_model.set_piece(2, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(4, 3, king_w)
        com_model.set_piece(2, 7, bishop_w)
        com_model.set_piece(5, 3, rook_b)
        com_model.set_piece(2, 2, rook_w)
        com_model.set_piece(6, 1, rook_w)
        com_model.set_piece(2, 5, bishop_b)
        com_model.set_piece(1, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(6, 3, queen_b)
        com_model.set_piece(6, 4, queen_b)
        com_model.set_piece(6, 2, queen_b)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(3, 3, king_w)
        com_model.set_piece(4, 4, queen_b)
        com_model.set_piece(4, 2, rook_b)
        com_model.set_piece(1,5, knight_b)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(1, 3, pawn_w)
        com_model.set_piece(1, 2, pawn_w)
        com_model.set_piece(0, 2, bishop_w)
        com_model.set_piece(0, 4, bishop_w)
        com_model.set_piece(3, 6, queen_b)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        com_model.set_next_player()
        com_model.set_piece(0, 3, king_b)
        com_model.set_piece(6, 3, queen_w)
        com_model.set_piece(6, 4, queen_w)
        com_model.set_piece(6, 2, queen_w)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        com_model.set_piece(0, 3, king_b)
        com_model.set_piece(1, 3, pawn_b)
        com_model.set_piece(1, 2, pawn_b)
        com_model.set_piece(0, 2, bishop_b)
        com_model.set_piece(0, 4, bishop_b)
        com_model.set_piece(3, 6, queen_w)
        self.assertTrue(com_model.is_complete())



    def test_move(self):
        pass

    def test_undo(self):
        pass


class chess_valid(unittest.TestCase):

    def test_piece(self):
        model = ChessModel
        rook = Rook(model.current_player)
        model.board = clear()
        model.set_piece(model,4, 3, rook)
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
        model.board = clear()

    def test_pawn(self):
        pass

    def test_knight(self):
        pass

    def test_bishop(self):
        model = ChessModel
        bishop = Bishop(model.current_player)
        model.board = clear()
        model.set_piece(model, 5, 3, bishop)
        model.set_piece(model, 3, 5, bishop)
        move = Move(5, 3, 7, 1)
        self.assertTrue(bishop.is_valid_move(move, model.board))
        move = Move(5, 3, 4, 4)
        self.assertTrue(bishop.is_valid_move(move, model.board))
        move = Move(5, 3, 2, 6)
        self.assertFalse(bishop.is_valid_move(move, model.board))
        move = Move(5, 3, 0, 3)
        self.assertFalse(bishop.is_valid_move(move, model.board))
        move = Move(5, 3, 4, 6)
        self.assertFalse(bishop.is_valid_move(move, model.board))
        model.board = clear()

    def test_rook(self):
        model = ChessModel
        rook = Rook(model.current_player)
        model.board = clear()
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
        model.board = clear()

    def test_king(self):
        model = ChessModel
        king = King(model.current_player)
        model.board = clear()
        model.set_piece(model, 5, 3, king)
        move = Move(5, 3, 7, 3)
        self.assertFalse(king.is_valid_move(move, model.board))
        move = Move(5, 3, 4, 3)
        self.assertTrue(king.is_valid_move(move, model.board))
        move = Move(5, 3, 5, 2)
        self.assertTrue(king.is_valid_move(move, model.board))
        move = Move(5, 3, 4, 2)
        self.assertTrue(king.is_valid_move(move, model.board))
        model.board = clear()

    def test_queen(self):
        pass
