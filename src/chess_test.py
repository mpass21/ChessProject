import unittest
from chess_model import ChessModel, MoveValidity
from move import Move
from player import Player
from chess_piece import ChessPiece
from pawn import Pawn
from queen import Queen
from knight import Knight
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





    def setUp(self):
        self.model = ChessModel()

    #testing is valid
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

    #test Knight
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
    def test_move_check_undo(self):
        self.undoModel = ChessModel()  

        

        move = Move(6, 5, 5, 5)
        move2 = Move(1, 4, 2, 4)
        move3 = Move(6, 0, 5, 0)
        moveCheck = Move(0,3,4,7)
        

        self.undoModel.move(move)  
        self.undoModel.move(move2)
        self.undoModel.move(move3)
        base = self.undoModel.copy_board(self.undoModel.get_board())
        self.undoModel.move(moveCheck)

        self.undoModel.undo()
        self.assertEqual(base, self.undoModel.board)
    
    def test_multiple_undo(self):
        self.undoModel = ChessModel()  
        base = self.undoModel.copy_board(self.undoModel.get_board()) 
        move = Move(6, 5, 5, 5)
        move2 = Move(1, 4, 2, 4)
        move3 = Move(6, 0, 5, 0) 
        self.undoModel.move(move)  
        self.undoModel.move(move2)
        self.undoModel.move(move3)
        self.undoModel.undo()
        self.undoModel.undo()  
        self.undoModel.undo()
        self.assertEqual(base, self.undoModel.board)

    def test_one_undo(self):
        self.undoModel = ChessModel()  
        base = self.undoModel.copy_board(self.undoModel.get_board()) 
        move = Move(6, 2, 4, 2)
        self.undoModel.move(move)
        self.undoModel.undo()
        self.assertEqual(base, self.undoModel.board)

    def test_redo(self):
        self.undoModel = ChessModel()  
        base = self.undoModel.copy_board(self.undoModel.get_board()) 
        move = Move(6, 2, 7, 2)
        self.undoModel.move(move)
        self.undoModel.undo()  
        self.undoModel.move(move)
        self.undoModel.undo()  
        self.assertEqual(base, self.undoModel.board)

    def test_capture_undo(self):
        self.undoModel = ChessModel()
        move1 = Move(6,3,4,3)
        move2 = Move(1,4,3,4)
        capture = Move(4,3,3,4)
        self.undoModel.move(move1)
        self.undoModel.move(move2)
        base = self.undoModel.copy_board(self.undoModel.get_board()) 
        self.undoModel.move(capture)
        self.undoModel.undo()
        self.assertEqual(base, self.undoModel.board)
    
    def test_undo_max(self):
        self.undoModel = ChessModel()
        with self.assertRaises(Exception):
            self.undoModel.undo()

    def test_undo_promotion(self):
        self.undoModel = ChessModel()
        self.undoModel.set_piece(6, 0, None)
        self.undoModel.set_piece(7, 0, None)
        move = Move(1,0,7,0)
        move2 = Move(1,4,2,4)
        promote = Move(6,0,7,0)
        
        self.undoModel.move(move)
        self.undoModel.move(move2)
        base = self.undoModel.copy_board(self.undoModel.get_board())
        self.undoModel.move(promote)
        self.undoModel.undo()
        self.assertEqual(base, self.undoModel.board)
        
        


       

        


    


    

if __name__ == '__main__':
    unittest.main()
    
