BOARD_SIZE = 8
from piece import *

class Board:
    def __init__(self):
        self.board = []
        self.board_view = []
       
        for i in range(BOARD_SIZE):
            self.board.append([0]*BOARD_SIZE) 
        
        for i in range(BOARD_SIZE):
            self.board_view.append([0]*BOARD_SIZE) 
            
        self.white_pieces()
        self.black_pieces()
        self.board_shapes()
        
            
    def white_pieces(self):
        self.w_r_1 = Rook([7,0],True,chrs['w_rook'])
        val = self.w_r_1.get_place()
        self.board[val[0]][val[1]] = self.w_r_1
        
        self.w_kn_1 = Knight([7,1],True,chrs['w_knight'])
        val = self.w_kn_1.get_place()
        self.board[val[0]][val[1]] = self.w_kn_1
        
        self.w_b_1 = Bishop([7,2],True,chrs['w_bishop'])
        val = self.w_b_1.get_place()
        self.board[val[0]][val[1]] = self.w_b_1
        
        self.w_q_1 = Queen([7,3],True,chrs['w_queen'])
        val = self.w_q_1.get_place()
        self.board[val[0]][val[1]] = self.w_q_1
        
        self.w_kg_1 = King([7,4],True,chrs['w_king'])
        val = self.w_kg_1.get_place()
        self.board[val[0]][val[1]] = self.w_kg_1
        
        self.w_b_2 = Bishop([7,5],True,chrs['w_bishop'])
        val = self.w_b_2.get_place()
        self.board[val[0]][val[1]] = self.w_b_2
        
        self.w_kn_2 = Knight([7,6],True,chrs['w_knight'])
        val = self.w_kn_2.get_place()
        self.board[val[0]][val[1]] = self.w_kn_2
        
        self.w_r_2 = Rook([7,7],True,chrs['w_rook'])
        val = self.w_r_2.get_place()
        self.board[val[0]][val[1]] = self.w_r_2
        
        self.w_p_0 = Pawn([4,0],True,chrs['w_pawn'])
        val = self.w_p_0.get_place()
        self.board[val[0]][val[1]] = self.w_p_0
        
        self.w_p_1 = Pawn([6,1],True,chrs['w_pawn'])
        val = self.w_p_1.get_place()
        self.board[val[0]][val[1]] = self.w_p_1
        
        self.w_p_2 = Pawn([6,2],True,chrs['w_pawn'])
        val = self.w_p_2.get_place()
        self.board[val[0]][val[1]] = self.w_p_2
        
        self.w_p_3 = Pawn([6,3],True,chrs['w_pawn'])
        val = self.w_p_3.get_place()
        self.board[val[0]][val[1]] = self.w_p_3
        
        self.w_p_4 = Pawn([6,4],True,chrs['w_pawn'])
        val = self.w_p_4.get_place()
        self.board[val[0]][val[1]] = self.w_p_4
        
        self.w_p_5 = Pawn([6,5],True,chrs['w_pawn'])
        val = self.w_p_5.get_place()
        self.board[val[0]][val[1]] = self.w_p_5
        
        self.w_p_6 = Pawn([6,6],True,chrs['w_pawn'])
        val = self.w_p_6.get_place()
        self.board[val[0]][val[1]] = self.w_p_6
        
        self.w_p_7 = Pawn([6,7],True,chrs['w_pawn'])
        val = self.w_p_7.get_place()
        self.board[val[0]][val[1]] = self.w_p_7
        
    def black_pieces(self):
        self.b_r_1 = Rook([0,0],False,chrs['b_rook'])
        val = self.b_r_1.get_place()
        self.board[val[0]][val[1]] = self.b_r_1
        
        # self.b_kn_1 = Knight([0,1],False,chrs['b_knight'])
        # val = self.b_kn_1.get_place()
        # self.board[val[0]][val[1]] = self.b_kn_1
        
        # self.b_b_1 = Bishop([0,2],False,chrs['b_bishop'])
        # val = self.b_b_1.get_place()
        # self.board[val[0]][val[1]] = self.b_b_1
        
        # self.b_q_1 = Queen([0,3],False,chrs['b_queen'])
        # val = self.b_q_1.get_place()
        # self.board[val[0]][val[1]] = self.b_q_1
        
        # self.b_kg_1 = King([0,4],False,chrs['b_king'])
        # val = self.b_kg_1.get_place()
        # self.board[val[0]][val[1]] = self.b_kg_1
        
        # self.b_b_2 = Bishop([0,5],False,chrs['b_bishop'])
        # val = self.b_b_2.get_place()
        # self.board[val[0]][val[1]] = self.b_b_2
        
        # self.b_kn_2 = Knight([0,6],False,chrs['b_knight'])
        # val = self.b_kn_2.get_place()
        # self.board[val[0]][val[1]] = self.b_kn_2
        
        self.b_r_2 = Rook([0,7],False,chrs['b_rook'])
        val = self.b_r_2.get_place()
        self.board[val[0]][val[1]] = self.b_r_2
        
        # self.b_p_0 = Pawn([1,0],False,chrs['b_pawn'])
        # val = self.b_p_0.get_place()
        # self.board[val[0]][val[1]] = self.b_p_0
        
        self.b_p_1 = Pawn([1,1],False,chrs['b_pawn'])
        val = self.b_p_1.get_place()
        self.board[val[0]][val[1]] = self.b_p_1
        
        self.b_p_2 = Pawn([1,2],False,chrs['b_pawn'])
        val = self.b_p_2.get_place()
        self.board[val[0]][val[1]] = self.b_p_2
        
        self.b_p_3 = Pawn([1,3],False,chrs['b_pawn'])
        val = self.b_p_3.get_place()
        self.board[val[0]][val[1]] = self.b_p_3
        
        self.b_p_4 = Pawn([1,4],False,chrs['b_pawn'])
        val = self.b_p_4.get_place()
        self.board[val[0]][val[1]] = self.b_p_4
        
        self.b_p_5 = Pawn([1,5],False,chrs['b_pawn'])
        val = self.b_p_5.get_place()
        self.board[val[0]][val[1]] = self.b_p_5
        
        self.b_p_6 = Pawn([1,6],False,chrs['b_pawn'])
        val = self.b_p_6.get_place()
        self.board[val[0]][val[1]] = self.b_p_6
        
        self.b_p_7 = Pawn([1,7],False,chrs['b_pawn'])
        val = self.b_p_7.get_place()
        self.board[val[0]][val[1]] = self.b_p_7
    
    def board_shapes(self):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.board[y][x] == 0:
                    pass
                else:
                    self.board_view[y][x] = self.board[y][x].get_shape()

        for i in range(8):
            print(self.board_view[i])
            
            
    
    def move_from_to(self,place: list,move:list):
        y = place[0]
        x = place[1]
        if self.board[y][x] == 0:
            print("No Piece")
            return False
        else: 
            self.move(y,x,move)
    
    def pre_move(self,y,x):
        piece = self.board[y][x]
        to_remove = []
        move_limit = []
        piece.pre_move()
        posibilities = piece.get_move_options()
        for dir in posibilities:
            for val in dir:
                if val[0]==7 or val[1]==7:
                    move_limit.append(val)
                    break
                if self.board[val[0]][val[1]]:
                    move_limit.append(val)
                    break
        piece.move_limits(move_limit)
        pre_limit_real = piece.get_move_limit()
        for atack in move_limit:
            limit_color = self.board[atack[0]][atack[1]].get_color()
            if limit_color == piece.get_color():
                to_remove.append(atack)
        for remove in to_remove:
            pre_limit_real.remove(remove)
        piece.set_move_limit(pre_limit_real)
        
        
    def move(self,y,x,move: list):
        self.pre_move(y,x)
        piece = self.board[y][x]
        if piece.move(move):
            self.board[y][x] = 0
            self.board_view[y][x] = 0
            moved = piece.get_place()
            y = moved[0]
            x = moved[1]
            self.board[y][x] = piece
            self.board_view[y][x] = self.board[y][x].get_shape()
            print("---------Move--------")
            for i in range(8):
                print(self.board_view[i])
        else:
            return False
        
        
       
        
        
game = Board()

game.move_from_to((0,0),(3,0))