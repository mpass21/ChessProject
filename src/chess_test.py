import unittest
from chess_model import ChessModel, MoveValidity
from move import Move
from player import Player
from chess_piece import ChessPiece
from pawn import Pawn
from queen import Queen
from knight import Knight

class TestMoves(unittest.TestCase):
    def setUp(self):
        self.model = ChessModel()
    #universal tests
    def no_start_piece(self):
        move = Move(4,4,4,5)
        self.assertFalse(move)

    def test_valid_standard_move_white(self):
        self.model.__player = Player.WHITE
        move = Move(1, 0, 2, 0)
        self.assertTrue(self.model.is_valid_move(move))

    def test_valid_standard_move_black(self):
        self.model.__player = Player.BLACK
        move = Move(6, 0, 5, 0)
        self.assertTrue(self.model.is_valid_move(move))

    def test_invalid_move_same_position(self):
        self.model.__player = Player.WHITE
        move = Move(1, 0, 1, 0)
        self.assertFalse(self.model.is_valid_move(move))

    def test_invalid_move_diagonal(self):
        self.model.__player = Player.WHITE
        move = Move(1, 0, 2, 1)
        self.assertFalse(self.model.is_valid_move(move))

    #pawn tests
    def test_valid_capture(self):
        self.model.__player = Player.WHITE
        self.model.set_piece(3, 4, Pawn(Player.BLACK))
        self.model.set_piece(4, 3, Pawn(Player.WHITE))
        move = Move(4, 3, 3, 4)
        self.assertTrue(self.model.is_valid_move(move))

    def test_invalid_capture_own_piece(self):
        self.model.__player = Player.WHITE
        self.model.set_piece(3, 4, Pawn(Player.WHITE))
        move = Move(2, 3, 3, 4)
        self.assertFalse(self.model.is_valid_move(move))

    def test_valid_pawn_promotion(self):
        self.model.__player = Player.WHITE
        self.model.set_piece(6, 0, None)
        self.model.set_piece(7, 0, None)
        self.model.set_piece(6, 0, Pawn(Player.WHITE))
        move = Move(6, 0, 7, 0)
        self.model.move(move)
        self.assertTrue(isinstance(self.model.piece_at(7,0), Queen))

    def test_blocked_pawn(self):
        self.model.__player = Player.WHITE
        self.model.set_piece(5,3, Pawn(Player.WHITE))
        move = Move(6, 3, 5,3)
        self.assertFalse(self.model.is_valid_move(move))



    #testing queen
    def test_valid_diagonal_movement(self):
        self.model.set_piece(3,3,Queen(Player.WHITE))
        move = Move(3, 3, 5, 5)
        self.assertTrue(self.model.is_valid_move(move))

    def test_valid_horizontal_movement(self):
        self.model.set_piece(3,3, Queen(Player.WHITE))
        move = Move(3, 3, 3, 5)
        self.assertTrue(self.model.is_valid_move(move))

    def test_valid_vertical_movement(self):
        self.model.set_piece(3,3, Queen(Player.WHITE))
        move = Move(3, 3, 5, 3)
        self.assertTrue(self.model.is_valid_move(move))

    def test_block(self):
        self.model.set_piece(3,3, Queen(Player.WHITE))
        self.model.set_piece(4,4, Queen(Player.BLACK))
        move = Move(from_row=3, from_col=3, to_row=5, to_col=5)
        self.assertFalse(self.model.is_valid_move(move))

    def test_capture_enemy_piece(self):
        self.model.set_piece(3,3, Queen(Player.BLACK))
        self.model.set_piece(4,4, Queen(Player.WHITE))
        move = Move(from_row=3, from_col=3, to_row=4, to_col=4)
        self.assertTrue(self.model.is_valid_move(move))

    def test_no_valid_moves(self):
        self.model.set_piece(3,3, Queen(Player.WHITE))
        for row in range(2, 5):
            for col in range(2, 5):
                if row != 3 and col != 3:
                    self.model.set_piece(row, col, Queen(Player.WHITE))
        move = Move(3, 3, 4, 4)
        self.assertFalse(self.model.is_valid_move(move))

    def test_out_bounds(self):
        move = Move(3, 3, 8, 8)
        self.assertFalse(self.model.is_valid_move(move))
    
    #testing knigt
    def test_knight_moves(self):
        self.model.set_piece(4,4,Knight(Player.BLACK))
        self.model.set_piece(6,5, None)
        self.model.set_piece(6,3, None)
        self.model.set_piece(2,3, None)
        self.model.set_piece(2,5, None)
        self.model.set_piece(5,6, None)
        self.model.set_piece(6,2, None)
        move = Move(4,4, 6,5)
        move2 = Move(4,4,6,3)
        move3 = Move(4,4,2,3)
        move4 = Move(4,4,2,3)
        move5 = Move(4,4,5,6)
        move6 = Move(4,4,5,2)
        self.assertTrue(self.model.is_valid_move(move))
        self.assertTrue(self.model.is_valid_move(move2))
        self.assertTrue(self.model.is_valid_move(move3))
        self.assertTrue(self.model.is_valid_move(move4))
        self.assertTrue(self.model.is_valid_move(move5))
        self.assertTrue(self.model.is_valid_move(move6))

    def test_knight_jump(self):
        self.model.set_piece(4,4,Knight(Player.BLACK))
        self.model.set_piece(5,4,Pawn(Player.BLACK))
        self.model.set_piece(5,4,None)
        move = Move(4,4,6,5)
        self.assertTrue(self.model.is_valid_move(move))
    
    def test_knight_capture(self):
        self.model.set_piece(4,4,Knight(Player.BLACK))
        self.model.set_piece(5,6, Pawn(Player.BLACK))
        move = Move(4,4,5,6)
        self.assertTrue(move)

    def test_blocked_knight(self):
        self.model.set_piece(4,4,Knight(Player.BLACK))
        self.model.set_piece(5,6, Pawn(Player.BLACK))
        move = Move(4,4,5,6)
        self.assertFalse(self.model.is_valid_move(move))

    #testing undo
    


    

if __name__ == '__main__':
    unittest.main()
    
