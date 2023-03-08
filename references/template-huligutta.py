import sys

class Board:
    a = f = { 1:(), 2:(),3:() }
    origin = ()
    b = c = d = e = { 0:origin, 1:(),2:(),3:(),4:()}
    
    def __init__(self):
        print('Initialized board')

    def printBoard(self):
        print('\t*\t*\t'+str(self.origin)+'\t*\t*\t')
        print(str(self.a[1])+'\t'+str(self.b[1])+'\t'+str(self.c[1])+'\t\t'+str(self.d[1])+'\t'+str(self.e[1])+'\t'+str(self.f[1]))
        print(str(self.a[2])+'\t'+str(self.b[2])+'\t'+str(self.c[2])+'\t\t'+str(self.d[2])+'\t'+str(self.e[2])+'\t'+str(self.f[2]))
        print(str(self.a[3])+'\t'+str(self.b[3])+'\t'+str(self.c[3])+'\t\t'+str(self.d[3])+'\t'+str(self.e[3])+'\t'+str(self.f[3]))
        print('\t'+str(self.b[4])+'\t'+str(self.c[4])+'\t\t'+str(self.d[4])+'\t'+str(self.e[4]))

    def isAdjacent(self,pos1,pos2):
        if not ( self.isValid(pos1) and self.isValid(pos2) ):
            print('Not valid positions')
            return(-1)
        
        adj = 0
        alph = ('a','b','c','d','e','f')
        if pos1[0] == pos2[0]:
            if abs(int(pos1[1]) - int(pos2[1])) ==1:
                adj =1
        else:
            if abs(alph.index(pos1[0])-alph.index(pos2[0])) == 1:
                if pos1[1] == pos2[1]:
                    adj =1

        return(adj)
    
    def isValid(self,pos):
        valid = 0
        if isinstance(pos, str):
            if len(pos) ==2:
                if pos[0] in 'af':
                    if pos[1] in '123':
                        valid = 1
                if pos[0] in 'bcde':
                    if pos[1] in '01234':
                        valid = 1
        return(valid)

class Position(Board):
    location = ''
    content = # (want this to be an animal/empty only)
    def __init__(self,alphabet,number):
        address = alphabet+number
        try:
            self.isValid(address)>0 :
            location = address
        except:
            print('Tried initializing position with invalid location') 

    def place(self,Animal):
        pass

    def get_neighbors(self):
        pass

    def get_captures(self):
        pass


    
class Piece(Board):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def adjacent(self, newposition):
        pass
        
class Tiger(Piece):
    def move(self,newposition):
        pass

    def capture(self,newposition):
        pass

class Goat(Piece):
    inplay =0
    def move(self,newposition):
        pass

    def place(self,position):
        pass


