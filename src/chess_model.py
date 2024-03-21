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
    """
    Chess Model that runs a chess game through a gui

    parameters:
        no parameters taken in

    raises:
        UndoException: raises the exception if undoing to many times
        ValueError: raises value error if piece is being set outside of row bounds
        TypeError: raises type error  
    """
    def __init__(self):
        """creates a instance of chessModel and sets all pieces to resemble a chessboard"""
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
        self.ai = False
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
        """Return the amount of rows in the board"""
        return self.__nrows

    @property
    def ncols(self):
        """Returns the amount of columns in the board"""
        return self.__ncols

    @property
    def current_player(self):
        """returns the current player"""
        return self.__player

    @property
    def messageCode(self):
        "returns the state of the message code"
        return self.__message_code

    def is_complete(self):
        """
        tests to see if the current player is in checkmate

        returns:
            True if the current player is in check
            False if the current player is not in checkmate
        """
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
                                        if not self.in_check(self.current_player, testBoard):
                                            return False
        return True
    
    def is_valid_move(self, move):
        """
        takes a move and sees if it is a valid move on self.board

        parameters:
            Move: a move object with the desired move

        returns:
            True: if the move is a valid move for the piece and board
            False: if the move is not a valid move for that piece and board
        """

        start_row, start_col = move.from_row, move.from_col
        piece = self.board[start_row][start_col]
        if not piece:   
            return False
        
        testBoard = self.copy_board(self.board)
        self.move_piece_test(testBoard, move)
        if self.in_check(self.current_player,testBoard):
            return False
        return piece.is_valid_move(move, self.board)

    def move_piece_test(self, board, move):
        """moves a piece on a given board

        parameters:
            Board: the board that move wants to be done on, a list of lists
            Move:  the move object that specifices what piece wants to be move where
        """
        piece = board[move.from_row][move.from_col]
        board[move.to_row][move.to_col] = piece
        board[move.from_row][move.from_col] = None
    
    def in_check(self,player, board=None):
        """checks if piece is in check based on the given parameters

            parameters:
                Board: a list of lists that represents a chess board
            
            returns: 
                True: if there if the player on given board is not in check
                False: if player on given board is in check
        """
        
        #sets board to self.board if no specific board is given
        if board is None:
            board = self.board

        #finding the players king on the board
        kingRow = None
        kingCol = None
        for row in range(8):
            for col in range(8):
                if isinstance(board[row][col], King) and board[row][col].player == player:
                    kingRow = row
                    kingCol = col
                    break
        
        #checking to make sure there are no knights attacking the king
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

        #checking if any pawns are attacking the king
        if player== Player.WHITE:
            pawn_moves = (-1, -1), (-1, 1)
        else:
            pawn_moves = (1, 1), (1, -1)

        for row, col in pawn_moves:
            attack_row, attack_col = kingRow + row, kingCol + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], Pawn) and board[attack_row][attack_col].player != player:
                    return True

        #checking if a queen or bishop is attacking the king from a diagonal position
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

        #checking if rook or queen is attacking from a horizontal/vertical position
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
        """a method that copys given board and appends it to a list
        
            parameter:
                board: a list of lists representing a chess board
        """
        copied_board = self.copy_board(board)
        self.moveList.append(copied_board)

    def move(self, move):
        """
            handles a given move and applys it to self.board. Also will promote a pawn if it reaches the end of the board

            parameter:
                move: a object that contains start location and end location
        """
        #checks if move is moving pawn to end of board
        if str(self.piece_at(move.from_row, move.from_col)) == 'Pawn' and (move.to_row == 0 or move.to_row == 7):

            #replaces pawn with queen
            self.set_piece(move.to_row, move.to_col, Queen(self.current_player))
        else:

            #moves piece
            self.set_piece(move.to_row, move.to_col, self.piece_at(move.from_row, move.from_col))
        self.board[move.from_row][move.from_col] = None

        #updates moveList and changes player
        self.updateMoveList(self.board)
        self.set_next_player()
              
    def piece_at(self, row: int, col: int):
        """takes a position on self.board and returns the piece at the location
        
            parameters:
                Row: a int that specifies the desired row of piece
                Col: a int that specifies the desired col of the piece
            
            returns:
                None: returns None if no piece is found
                Piece: returns a piece object if one is found
        """

        #if the location is in bounds returns the piece
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]

    def set_next_player(self):
        """changes the current player to opposing player"""
        self.__player = Player.next(self.__player)
        if not self.is_complete():
            if self.__player == Player.BLACK and self.ai is True:
                board = self.copy_board(self.board)
                move = self.ai_move(board)
                self.move(move)

    def ai_move(self, board):
            """logic behind the ai player that plays as black if desired

                parameters:
                    Board: a list of lists that represents a chess board
                
                returns: 
                    a calculated move that helps the artificial player
            """

            #checks if the ai is in check, if so the move generated prioritises leaving check
            piece_lst = [Pawn, Queen, Rook, Bishop, Knight, King]
            if self.in_check(Player.BLACK):
                for i in range(0, 8):
                    for j in range(0, 8):
                        for piece in piece_lst:
                            if isinstance(self.piece_at(i, j), piece):
                                if self.piece_at(i, j).player == Player.BLACK:
                                    for x in range(0, 8):
                                        for y in range(0, 8):
                                            move = Move(i, j, x, y)
                                            if self.piece_at(i, j).is_valid_move(move, board):
                                                testBoard = self.copy_board(self.board)
                                                self.move_piece_test(testBoard, move)
                                                if not self.in_check(Player.BLACK, testBoard):
                                                    return move
            
            for i in range(0, 8):
                for j in range(0, 8):
                    for piece in piece_lst:
                        if isinstance(self.piece_at(i, j), piece):
                            if self.piece_at(i, j).player == Player.BLACK:
                                for x in range(0, 8):
                                    for y in range(0, 8):
                                        move = Move(i, j, x, y)
                                        if self.piece_at(i, j).is_valid_move(move, board):
                                            testBoard = self.copy_board(self.board)
                                            self.move_piece_test(testBoard, move)
                                            if not self.in_check(Player.BLACK, testBoard):
                                                if self.in_check(Player.WHITE, testBoard):
                                                    return move
            for piece in piece_lst:
                for j in range(0, 8):
                    for i in range(0, 8):
                        if isinstance(self.piece_at(i, j), piece):
                            if self.piece_at(i, j).player == Player.BLACK:
                                if self.in_danger(i, j, self.board, Player.BLACK):
                                    for x in range(7, -1, -1):
                                        for y in range(7, -1, -1):
                                            move = Move(i, j, x, y)
                                            if self.piece_at(i, j).is_valid_move(move, board):
                                                testBoard = self.copy_board(self.board)
                                                self.move_piece_test(testBoard, move)
                                                if not self.in_check(Player.BLACK, testBoard):
                                                    if self.piece_at(x, y) is not None:
                                                        return move
                                    for x in range(0, 8):
                                        for y in range(0, 8):
                                            move = Move(i, j, x, y)
                                            if self.piece_at(i, j).is_valid_move(move, board):
                                                testBoard = self.copy_board(self.board)
                                                self.move_piece_test(testBoard, move)
                                                if not self.in_check(Player.BLACK, testBoard):
                                                    if not self.in_danger(x, y, testBoard, Player.BLACK):
                                                        return move
            for piece in piece_lst:
                for j in range(0, 8):
                    for i in range(0, 8):
                        if isinstance(self.piece_at(i, j), piece):
                            if self.piece_at(i, j).player == Player.BLACK:
                                for x in range(0, 8):
                                    for y in range(0, 8):
                                        move = Move(i, j, x, y)
                                        if self.piece_at(i, j).is_valid_move(move, board):
                                            testBoard = self.copy_board(self.board)
                                            self.move_piece_test(testBoard, move)
                                            if not self.in_check(Player.BLACK, testBoard):
                                                if self.piece_at(x, y) is not None:
                                                    return move
            for piece in piece_lst:
                for j in range(0, 8):
                    for i in range(0, 8):
                        if isinstance(self.piece_at(i, j), piece):
                            if self.piece_at(i, j).player == Player.BLACK:
                                for x in range(7, -1, -1):
                                    for y in range(7, -1, -1):
                                        move = Move(i, j, x, y)
                                        if self.piece_at(i, j).is_valid_move(move, board):
                                            testBoard = self.copy_board(self.board)
                                            self.move_piece_test(testBoard, move)
                                            if not self.in_check(Player.BLACK, testBoard):
                                                if not self.in_danger(x, y, testBoard, Player.BLACK):
                                                    return move
            for x in range(7, -1, -1):
                for y in range(7, -1, -1):
                    move = Move(i, j, x, y)
                    if self.piece_at(i, j).is_valid_move(move, board):
                        testBoard = self.copy_board(self.board)
                        self.move_piece_test(testBoard, move)
                        if not self.in_check(Player.BLACK, testBoard):
                            if not self.in_danger(x, y, testBoard, Player.BLACK):
                                return move
            for x in range(7, -1, -1):
                for y in range(7, -1, -1):
                    move = Move(i, j, x, y)
                    if self.piece_at(i, j).is_valid_move(move, board):
                        testBoard = self.copy_board(self.board)
                        self.move_piece_test(testBoard, move)
                        if not self.in_check(Player.BLACK, testBoard):
                            return move
    
    def in_danger(self, x, y, board, player):
        """checks if piece is in danger if so it returns True

            parameters: 
                x: the row cordinate for the piece to be tested
                y: the col cordinate for the piece in danger
                board: a list of lists representing the chess board the piece is on
                player: the player that is being tested

            returns: 
                True: if the piece is in danger
                False: if the piece is not in danger
                
        """
        piece_row = x
        piece_col = y

        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for row, col in knight_moves:
            attack_row, attack_col = piece_row + row, piece_col + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], Knight) and board[attack_row][attack_col].player != player:
                    return True

        king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row, col in king_moves:
            attack_row, attack_col = piece_row + row, piece_col + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], King) and board[attack_row][attack_col].player != player:
                    return True

        pawn_moves = (1, 1), (1, -1)

        for row, col in pawn_moves:
            attack_row, attack_col = piece_row + row, piece_col + col
            if 0 <= attack_row < 8 and 0 <= attack_col < 8:
                if isinstance(board[attack_row][attack_col], Pawn) and board[attack_row][attack_col].player != player:
                    return True

        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diagonal_directions:
            for i in range(1, 8):
                new_row, new_col = piece_row + i * dr, piece_col + i * dc
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
                new_row, new_col = piece_row + i * dr, piece_col + i * dc
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
    
    def set_piece(self, row: int, col: int, piece: ChessPiece):
        """sets a piece at a specific locatin on self.board

            parameters:
                row: the specific row where the piece is to be placed on
                col: the specific collumn where the piece is to be placed on

            raises:
                UndoException: raises the exception if undoing to many times
                ValueError: raises value error if piece is being set outside of row bounds
                TypeError: raises type error  
        """

        #checks if desired location is within bounds and a piece, if not it raises apropriate error
        if 0 <= row < 8:
            if 0 <= col < 8:
                if piece is None or ChessPiece:
                    self.board[row][col] = piece
                else:
                    raise TypeError
            else:
                raise ValueError
        else:
            raise ValueError
        
    def copy_board(self, board):
        """creates a copy of a given board
        
            parameter:
                board: a list of lists that represents a chess board
            
            returns:
                a list of lists that is a copy of board taken in as parameter
        """
        newBoard = []
        for row in board:
            newBoard.append(copy.copy(row))
        return newBoard
    
    def undo(self):
        """undoes the most recent move
        
            raises:
                UndoException: raises error if there are no more moves to be undone
        """
        if not self.ai:
            if len(self.moveList) > 1:
                self.moveList.pop()
                self.board = self.copy_board(self.moveList[-1])
                self.set_next_player()
            else:
                raise UndoException()
        elif len(self.moveList) > 1:
            self.moveList.pop()
            self.moveList.pop()
            self.board = self.copy_board(self.moveList[-1])
        else:
            raise UndoException()

    def get_board(self):
        """returns the current state of the game as a list of lists"""
        return self.board