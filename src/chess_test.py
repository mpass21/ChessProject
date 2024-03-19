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
        check_model = ChessModel()
        rook_w = Rook(check_model.current_player)
        queen_w = Queen(check_model.current_player)
        bishop_w = Bishop(check_model.current_player)
        knight_w = Knight(check_model.current_player)
        pawn_w = Pawn(check_model.current_player)
        king_w = King(check_model.current_player)
        check_model.set_next_player()
        rook_b = Rook(check_model.current_player)
        queen_b = Queen(check_model.current_player)
        bishop_b = Bishop(check_model.current_player)
        knight_b = Knight(check_model.current_player)
        pawn_b = Pawn(check_model.current_player)
        king_b = King(check_model.current_player)
        check_model.set_next_player()
        check_model.board = clear()
        '''check rook'''
        check_model.set_piece(2, 0, king_w)
        check_model.set_piece(2, 3, rook_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''not check, rook blocked'''
        check_model.set_piece(2, 0, king_w)
        check_model.set_piece(2, 5, rook_b)
        check_model.set_piece(2, 3, bishop_w)
        self.assertFalse(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''check queen row'''
        check_model.set_piece(2, 0, king_w)
        check_model.set_piece(2, 3, queen_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''not check queen row blocked'''
        check_model.set_piece(3, 2, king_w)
        check_model.set_piece(1, 4, queen_b)
        check_model.set_piece(2, 3, queen_w)
        self.assertFalse(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''check queen diagonal'''
        check_model.set_piece(2, 0, king_w)
        check_model.set_piece(0, 2, queen_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''check bishop'''
        check_model.set_piece(6, 3, king_w)
        check_model.set_piece(2, 7, bishop_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        '''not check, bishop blocked'''
        check_model.set_piece(3, 6, rook_w)
        self.assertFalse(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''check pawn'''
        check_model.set_piece(3, 5, king_w)
        check_model.set_piece(4, 6, pawn_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''basic not in check'''
        check_model.set_piece(3, 5, king_w)
        check_model.set_piece(4, 6, pawn_w)
        self.assertFalse(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        '''check knight'''
        check_model.set_piece(3, 5, king_w)
        check_model.set_piece(4, 7, knight_b)
        self.assertTrue(check_model.in_check(check_model.current_player))
        check_model.board = clear()
        check_model.set_next_player()
        '''other player, check'''
        check_model.set_piece(3, 5, king_b)
        check_model.set_piece(4, 7, knight_w)
        self.assertTrue(check_model.in_check(check_model.current_player))



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
        '''king cant move, move bishop to capture'''
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(0, 1, bishop_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(0, 2, rook_w)
        com_model.set_piece(2, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        self.assertEqual(com_model.current_player, Player.WHITE)
        com_model.board = clear()
        '''king cant move, move knight to block'''
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(0, 2, rook_w)
        com_model.set_piece(0, 4, pawn_w)
        com_model.set_piece(0, 2, pawn_w)
        com_model.set_piece(1, 4, knight_w)
        com_model.set_piece(6, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        self.assertEqual(com_model.current_player, Player.WHITE)
        com_model.board = clear()
        '''King can move'''
        com_model.set_piece(4, 3, king_w)
        com_model.set_piece(2, 7, bishop_w)
        com_model.set_piece(5, 3, rook_b)
        com_model.set_piece(2, 2, rook_w)
        com_model.set_piece(6, 1, rook_w)
        com_model.set_piece(2, 5, bishop_b)
        com_model.set_piece(1, 3, queen_b)
        self.assertFalse(com_model.is_complete())
        self.assertEqual(com_model.current_player, Player.WHITE)
        com_model.board = clear()
        '''king cant move, no piece to help'''
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(6, 3, queen_b)
        com_model.set_piece(6, 4, queen_b)
        com_model.set_piece(6, 2, queen_b)
        self.assertTrue(com_model.is_complete())
        self.assertEqual(com_model.current_player, Player.WHITE)
        com_model.board = clear()
        '''king cant move, rook captures'''
        com_model.set_piece(3, 3, king_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(4, 4, queen_b)
        com_model.set_piece(4, 2, rook_b)
        com_model.set_piece(1,5, knight_b)
        self.assertFalse(com_model.is_complete())
        com_model.board = clear()
        '''king cant move, pawn captures'''
        com_model.set_piece(3, 3, king_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(5, 5, pawn_w)
        com_model.set_piece(4, 4, queen_b)
        com_model.set_piece(1, 5, knight_b)
        self.assertFalse(com_model.is_complete())
        com_model.board = clear()
        '''king cant move, rook blocked'''
        com_model.set_piece(3, 3, king_w)
        com_model.set_piece(0, 4, rook_w)
        com_model.set_piece(2, 4, pawn_w)
        com_model.set_piece(4, 4, queen_b)
        com_model.set_piece(4, 2, rook_b)
        com_model.set_piece(1, 5, knight_b)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        '''stalemate'''
        com_model.set_piece(0, 3, king_w)
        com_model.set_piece(1, 3, bishop_b)
        com_model.set_piece(1, 1, rook_b)
        com_model.set_piece(0, 2, bishop_b)
        com_model.set_piece(0, 4, bishop_b)
        com_model.set_piece(1, 5, rook_b)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        '''checkmate 2 knights'''
        com_model.set_piece(0, 0, king_w)
        com_model.set_piece(0, 1, rook_w)
        com_model.set_piece(1, 1, pawn_w)
        com_model.set_piece(1, 0, rook_w)
        com_model.set_piece(2, 1, knight_b)
        com_model.set_piece(1, 2, knight_b)
        com_model.set_piece(2, 4, rook_w)
        com_model.set_piece(3, 2, rook_w)
        self.assertTrue(com_model.is_complete())
        com_model.board = clear()
        com_model.set_next_player()
        '''other player, checkmate 3 Queens'''
        com_model.set_piece(0, 3, king_b)
        com_model.set_piece(6, 3, queen_w)
        com_model.set_piece(6, 4, queen_w)
        com_model.set_piece(6, 2, queen_w)
        self.assertTrue(com_model.is_complete())
        self.assertEqual(com_model.current_player, Player.BLACK)
        com_model.board = clear()
        '''other player, not checkmate'''
        com_model.set_piece(0, 3, king_b)
        com_model.set_piece(1, 3, pawn_b)
        com_model.set_piece(1, 2, pawn_b)
        com_model.set_piece(0, 2, bishop_b)
        com_model.set_piece(0, 4, bishop_b)
        com_model.set_piece(3, 4, rook_b)
        com_model.set_piece(3, 6, queen_w)
        self.assertFalse(com_model.is_complete())

    def test_move(self):
        move_model = ChessModel()
        pawn = Pawn(move_model.current_player)
        move_model.board = clear()
        move_model.set_piece(2,4,pawn)
        move = Move(2,4, 1,4)
        move_model.move(move)
        self.assertEqual(move_model.piece_at(1,4), pawn)
        self.assertEqual(move_model.piece_at(2, 4), None)
        self.assertEqual(move_model.current_player, Player.BLACK)
        move = Move(1, 4, 0, 4)
        move_model.move(move)
        self.assertTrue(isinstance(move_model.piece_at(0, 4), Queen))




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
        self.assertTrue(isinstance(model.piece_at(model, 5,3), ChessPiece))
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
        self.assertTrue(isinstance(model.piece_at(model, 4, 3), ChessPiece))
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
        self.assertTrue(isinstance(model.piece_at(model, 5, 3), ChessPiece))
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
