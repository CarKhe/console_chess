BOARD_SIZE = 8
chrs = {
    'w_checker': u'\u25FB',
    'w_pawn': u'\u265F',
    'w_rook': u'\u265C',
    'w_knight': u'\u265E',
    'w_bishop': u'\u265D',
    'w_king': u'\u265A',
    'w_queen': u'\u265B',
    'b_checker': u'\u25FC',
    'b_pawn': u'\u2659',
    'b_rook': u'\u2656',
    'b_knight': u'\u2658',
    'b_bishop': u'\u2657',
    'b_king': u'\u2654',
    'b_queen': u'\u2655'
}


class Piece:
    #White == True Black == False
    def __init__(self,place: list,color: bool,shape:str):
        self.__place = place
        self.__color = color
        self.__shape = shape
        
    def get_place(self):
        return self.__place
    
    def get_color(self):
        return self.__color
    
    def get_shape(self):
        return self.__shape
    
    def set_place(self,new_place):
        self.__place = new_place
    
    def set_color(self,new_color):
        self.__color = new_color
    
    def set_shape(self,new_shape):
        self.__shape = new_shape
    
    def move(self):
        print("piece moved")


class King(Piece):
    def __init__(self,place: list,color: bool,shape:str):
        super().__init__(place, color, shape)
        self.move_options = ""
    
    def get_move_options(self):
        return self.move_options
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y= place[0]
        x = place[1]
        self.move_options = [[y-1,x-1],
            [y-1,x],[y-1,x+1],[y,x-1],[y,x+1],[y+1,x-1]
            ,[y+1,x],[y+1,x+1]]
        for place in self.move_options:
            if place[0]<=-1 or place[1]<=-1 or (place[0]>=BOARD_SIZE) or (place[1]>=BOARD_SIZE):
                to_remove.append(place)
        for delete in to_remove:
            self.move_options.remove(delete)
        
        
    def move(self,move):
        self.pre_move()
        for pre_move in self.move_options:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False
    
    def castle(self,move):
        place  = self.get_place()
        if place == [0,4] or place == [7,4]:
            if move:           #(0-0-0)
                self.set_place([place[0],place[1]-2])
            else:              #(0-0)
                self.set_place([place[0],place[1]+2])
        return False
                

class Pawn(Piece):
    def __init__(self,place: list,color: bool,shape:str):
        super().__init__(place, color, shape)
        self.move_options = ""
        
    def get_move_options(self):
        return self.move_options
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y = place[0]
        x = place[1]
        if self.get_color(): 
            self.move_options = [[y-1,x-1],[y-1,x],[y-1,x+1]]
        else:
            self.move_options = [[y+1,x-1],[y+1,x],[y+1,x+1]]
        for place in self.move_options:
            if place[0]<=-1 or place[1]<=-1 or (place[0]>=BOARD_SIZE) or (place[1]>=BOARD_SIZE):
                to_remove.append(place)       
        for delete in to_remove:
            self.move_options.remove(delete)
            
    def move(self,move):
        self.pre_move()
        for pre_move in self.move_options:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False
    
    def double_move(self):
        place = self.get_place()
        y = place[0]
        x = place[1]
        if self.get_color():
            if place[0] == 6:
                self.set_place([y-2,x])
                return True
        else:
            if place[0] == 1:
                self.set_place([y+2,x])
                return True
        return False
   
            
class Rook(Piece): 
    def __init__(self, place: list, color: bool, shape: str):
        super().__init__(place, color, shape)
        self.move_options = ""
        self.move_limit = []
    
    def get_move_options(self):
        return self.move_options
    
    def get_move_limit(self):
        return self.move_limit
    
    def set_move_limit(self,limit: list):
        self.move_limit = limit
    
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y = place[0]
        x = place[1]
        self.move_options = [[],[],[],[]]
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options[0].append((y-add,x))
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options[1].append((y,x+add))
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options[2].append((y+add,x))
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options[3].append((y,x-add))
        for place in self.move_options:
            if place[0][0]<=-1 or place[0][1]<=-1 or (place[0][0]>=BOARD_SIZE) or (place[0][1]>=BOARD_SIZE):
                to_remove.append(place)       
        for delete in to_remove:
            self.move_options.remove(delete)
        
    
    def move_limits(self,limits:list):
        moves_allowed = []
        for vars in range(len(limits)):
            limit = limits[vars]
            for vals in self.move_options[vars]: 
                if (limit[0]>=vals[0] and limit[1]>=vals[1]):
                    moves_allowed.append(vals)
        self.move_limit = moves_allowed
  
    def move(self,move):
        for pre_move in self.move_limit:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False
    
    def castle(self,move):
        place  = self.get_place()
        y = place[0]
        x = place[1]
        if self.get_color(): #True = White False = Black
            if place == [7,0] or place == [7,7]:
                if move:           #(0-0-0)
                    self.set_place([y,x+3])
                    return True
                else:              #(0-0)
                    self.set_place([y,x-2])
                    return True
        else:
            if place == [0,0] or place == [0,7]:
                if move:           #(0-0-0)
                    self.set_place([y,x+3])
                    return True
                else:              #(0-0)
                    self.set_place([y,x-2])
                    return True
        return False
            
                      
class Bishop(Piece):
    def __init__(self, place: list, color: bool, shape: str):
        super().__init__(place, color, shape)
        self.move_options = ""
    
    def get_move_options(self):
        return self.move_options
    
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y = place[0]
        x = place[1]
        self.move_options = []
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options.append([y-add,x-add])
            self.move_options.append([y-add,x+add])
            self.move_options.append([y+add,x+add])
            self.move_options.append([y+add,x-add])
        for place in self.move_options:
            if place[0]<=-1 or place[1]<=-1 or (place[0]>=BOARD_SIZE) or (place[1]>=BOARD_SIZE):
                to_remove.append(place)       
        for delete in to_remove:
            self.move_options.remove(delete)
            
        print(self.move_options)
            
    def move(self,move):
        self.pre_move()
        for pre_move in self.move_options:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False


class Knight(Piece):
    def __init__(self, place: list, color: bool, shape: str):
        super().__init__(place, color, shape)
        self.move_options = ""
    
    def get_move_options(self):
        return self.move_options
    
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y = place[0]
        x = place[1]
        self.move_options = [[y-1,x-2],[y-2,x-1],[y-2,x+1],
            [y-1,x+2],[y+1,x+2],[y+2,x+1],[y+2,x-1],[y+1,x-2]]
    
        for place in self.move_options:
            if place[0]<=-1 or place[1]<=-1 or (place[0]>=BOARD_SIZE) or (place[1]>=BOARD_SIZE):
                to_remove.append(place)       
        for delete in to_remove:
            self.move_options.remove(delete)
            
            
    def move(self,move):
        self.pre_move()
        for pre_move in self.move_options:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False


class Queen(Piece):
    def __init__(self, place: list, color: bool, shape: str):
        super().__init__(place, color, shape)
        self.move_options = ""
    
    def get_move_options(self):
        return self.move_options
    
    
    def pre_move(self):
        place = self.get_place()
        to_remove = []
        y = place[0]
        x = place[1]
        self.move_options = []
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options.append([y-add,x])
            self.move_options.append([y,x+add])
            self.move_options.append([y+add,x])
            self.move_options.append([y,x-add])
        for add in range(BOARD_SIZE):
            add +=1
            self.move_options.append([y-add,x-add])
            self.move_options.append([y-add,x+add])
            self.move_options.append([y+add,x+add])
            self.move_options.append([y+add,x-add])

        for place in self.move_options:
            if place[0]<=-1 or place[1]<=-1 or (place[0]>=BOARD_SIZE) or (place[1]>=BOARD_SIZE):
                to_remove.append(place)       
        for delete in to_remove:
            self.move_options.remove(delete)
            
        
            
    def move(self,move):
        self.pre_move()
        for pre_move in self.move_options:
            if pre_move == move:
                self.set_place(move)
                return True
            else:
                continue 
        return False










