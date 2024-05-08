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
        
        
        self.w_p_4 = Pawn([2,1],True,chrs['w_pawn'])
        val = self.w_p_4.get_place()
        self.board[val[0]][val[1]] = self.w_p_4
        
        self.w_p_5 = Pawn([5,6],True,chrs['w_pawn'])
        val = self.w_p_5.get_place()
        self.board[val[0]][val[1]] = self.w_p_5
        
        self.w_p_6 = Pawn([7,5],True,chrs['w_pawn'])
        val = self.w_p_6.get_place()
        self.board[val[0]][val[1]] = self.w_p_6
        
        self.w_p_7 = Pawn([4,3],True,chrs['w_pawn'])
        val = self.w_p_7.get_place()
        self.board[val[0]][val[1]] = self.w_p_7
        
    def black_pieces(self):
        self.b_r_1 = Pawn([1,1],False,chrs['b_pawn'])
        val = self.b_r_1.get_place()
        self.board[val[0]][val[1]] = self.b_r_1
        
       
    
    def board_shapes(self):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if self.board[y][x] == 0:
                    pass
                else:
                    self.board_view[y][x] = self.board[y][x].get_shape()
        
        #Board Shape in game
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
        if type(piece) is Queen or type(piece) is King:
            move_limit = [0,0,0,0,0,0,0,0]
        elif type(piece) is  Pawn:
            move_limit = [0,0,0]
        else:
            move_limit = [0,0,0,0]
        piece.pre_move()
        
        posibilities = piece.get_move_options()  
        pos = 0  
        print(posibilities)
        for dir in posibilities:
            for val in dir:
                
                if self.board[val[0]][val[1]]:
                    move_limit[pos] = val
                    break
            pos +=1

        for val in range(len(move_limit)):
            if posibilities[val] == []:
                move_limit[val] = []
            elif move_limit[val] == 0:
                move_limit[val] = posibilities[val][-1]
        print(move_limit)
        piece.move_limits(move_limit)
        pre_limit_real = piece.get_move_options() 
        for atack in move_limit:
            pos = move_limit.index(atack)
            try:
                limit_color = self.board[atack[0]][atack[1]].get_color()
            except:
                color = piece.get_color()
                if color:
                    limit_color = False
                else:
                    limit_color = True
            if limit_color == piece.get_color():
                pre_limit_real[pos].remove(atack)
        piece.set_move_options(pre_limit_real)
        
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

game.move_from_to((1,1),(2,2))






