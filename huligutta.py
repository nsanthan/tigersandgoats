'''
file: huligutta.py
Description: Board functionalities
'''

__author__ = "Clyde James Felix"
__email__ = "cjfelix.hawaii.edu"
__status__ = "Dev"

import numpy as np
import sys
import time
class Board:
    # Not used as an object, the functions are just used. The
    # dictionary below is the state of the game at any point.
    a = { 1:(), 2:(),3:() }
    f = { 1:(), 2:(),3:() }
    origin = ()
    b = { 0:origin, 1:(),2:(),3:(),4:()}
    c = { 0:origin, 1:(),2:(),3:(),4:()}
    d = { 0:origin, 1:(),2:(),3:(),4:()}
    e = { 0:origin, 1:(),2:(),3:(),4:()}
    
    def __init__(self):
        if not self.b[0]==() :
            self.origin = self.b[0]  
            self.c[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.e[0] = self.b[0] 
        if not self.c[0]==():
            self.origin = self.c[0]
            self.b[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.e[0] = self.b[0]
        if not self.d[0]==() :
            self.origin = self.d[0]
            self.c[0] = self.b[0] 
            self.b[0] = self.b[0] 
            self.e[0] = self.b[0]
        if not self.e[0]==() :
            self.origin = self.e[0]
            self.c[0] = self.b[0] 
            self.d[0] = self.b[0] 
            self.b[0] = self.b[0] 

        self.boardPositions = {'b0': self.b[0],'a1': self.a[1],'a2': self.a[2],'a3': self.a[3],
        'b1': self.b[1],'b2': self.b[2],'b3': self.b[3],'b4': self.b[4],
        'c1': self.c[1],'c2': self.c[2],'c3': self.c[3],'c4': self.c[4],
        'd1': self.d[1],'d2': self.d[2],'d3': self.d[3],'d4': self.d[4],
        'e1': self.e[1],'e2': self.e[2],'e3': self.e[3],'e4': self.e[4],
        'f1': self.f[1],'f2': self.f[2],'f3': self.f[3]}

    def boardToMatrix(self):
        boardToNumber = {                         'b0': 0, 
                  'a1': 1 , 'b1': 2 , 'c1': 3 , 'd1': 4 , 'e1': 5 , 'f1': 6 , 
                  'a2': 7 , 'b2': 8 , 'c2': 9 , 'd2': 10, 'e2': 11, 'f2': 12,
                  'a3': 13, 'b3': 14, 'c3': 15, 'd3': 16, 'e3': 17, 'f3': 18,
                            'b4': 19, 'c4': 20, 'd4': 21, 'e4': 22
                 }

        orderedBoard = np.empty((23,3))

        for key in boardToNumber:
            #print(key,self.boardPositions[key],boardToNumber[key])
            if   str(self.boardPositions[key]) == "()":
                orderedBoard[boardToNumber[key]] = [0, 0, 1]
            elif str(self.boardPositions[key]) == "X" :
                orderedBoard[boardToNumber[key]] = [1, 0, 0]
            elif str(self.boardPositions[key]) == "O":
                orderedBoard[boardToNumber[key]] = [0, 1, 0]    
            #    orderedBoard[boardToNumber[key]] = self.boardPositions[key]
        
        #print(orderedBoard)
        #convert = {"X": [1, 0, 0],
        #"O": [0, 1, 0],
        #"()": [0, 0, 1]}
        #print(orderedBoard)  
        #return 1
        return orderedBoard
        
    def clearBoard(self):
        a = { 1:(), 2:(),3:() }
        f = { 1:(), 2:(),3:() }
        origin = ()
        b = { 0:origin, 1:(),2:(),3:(),4:()}
        c = { 0:origin, 1:(),2:(),3:(),4:()}
        d = { 0:origin, 1:(),2:(),3:(),4:()}
        e = { 0:origin, 1:(),2:(),3:(),4:()}
        for i in self.a:
            if Position('a',str(i)).content() != ():
                Position('a',str(i)).place(())
        for i in self.b:
            if Position('b',str(i)).content() != ():
                Position('b',str(i)).place(())
        for i in self.c:
            if Position('c',str(i)).content() != ():
                Position('c',str(i)).place(())
        for i in self.d:
            if Position('d',str(i)).content() != ():
                Position('d',str(i)).place(())
        for i in self.e:
            if Position('e',str(i)).content() != ():
                Position('e',str(i)).place(())
        for i in self.f:
            if Position('f',str(i)).content() != ():
                Position('f',str(i)).place(())                
                       

    def printBoard(self):
    
        print('\t*\t*\t'+str(self.origin)+'\t*\t*\t')
        print(str(self.a[1])+'\t'+str(self.b[1])+'\t'+str(self.c[1])+'\t\t'+str(self.d[1])+'\t'+str(self.e[1])+'\t'+str(self.f[1]))
        print(str(self.a[2])+'\t'+str(self.b[2])+'\t'+str(self.c[2])+'\t\t'+str(self.d[2])+'\t'+str(self.e[2])+'\t'+str(self.f[2]))
        print(str(self.a[3])+'\t'+str(self.b[3])+'\t'+str(self.c[3])+'\t\t'+str(self.d[3])+'\t'+str(self.e[3])+'\t'+str(self.f[3]))
        print('\t'+str(self.b[4])+'\t'+str(self.c[4])+'\t\t'+str(self.d[4])+'\t'+str(self.e[4]))
                
    def isAdjacent(self,pos1,pos2):
        if not (self.isValid(pos1) and self.isValid(pos2)):
            return(-1)
        
        adj = 0
        alph = ('a','b','c','d','e','f')
        if pos1[0] in 'bcde' and pos1[1] == 0:
            if pos2[0] not in 'af':
                pos1[0]=pos2[0]
                
        if pos2[0] in 'bcde' and pos2[1] == 0:
            if pos2[0] not in 'af':
                pos2[0]=pos1[0]
            
        if pos1[0] == pos2[0]:
            if abs(int(pos1[1]) - int(pos2[1])) == 1:
                adj = 1

        if abs(alph.index(pos1[0])-alph.index(pos2[0])) == 1:
            if pos1[1] == pos2[1]:
                adj = 1

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
# Not a true object, but a bunch of functions engaged with the input
# position.  No need for instantiation. Board is inherited.
    
    def __init__(self,alphabet,number):
        address = alphabet + number
        self.alphabet = alphabet
        self.number = number
        try:
            assert(self.isValid(address)>0)
            self.location = address
        except:
            print('Tried initializing position with invalid location') 
    
    def content(self):
        if self.alphabet == 'a':
            cont = self.a[int(self.number)]
        if self.alphabet == 'b':
            cont = self.b[int(self.number)]
        if self.alphabet == 'c':
            cont = self.c[int(self.number)]
        if self.alphabet == 'd':
            cont = self.d[int(self.number)]
        if self.alphabet == 'e':
            cont = self.e[int(self.number)]
        if self.alphabet == 'f':
            cont = self.f[int(self.number)]
        return cont
    
    def place(self,Animal):
        if self.alphabet == 'a':
            self.a[int(self.number)] = Animal
            self.content = Animal
            
        if self.alphabet == 'b': 
            self.b[int(self.number)] = Animal
            self.content = Animal

        if self.alphabet == 'c':            
            self.c[int(self.number)] = Animal
            self.content = Animal
           
        if self.alphabet == 'd':            
            self.d[int(self.number)] = Animal
            self.content = Animal
          
        if self.alphabet == 'e':            
            self.e[int(self.number)] = Animal
            self.content = Animal
          
        if self.alphabet == 'f':            
            self.f[int(self.number)] = Animal    
            self.content = Animal

        if self.number == '0':
            self.b[0] = Animal  
            self.c[0] = Animal  
            self.d[0] = Animal  
            self.e[0] = Animal  
            self.content = Animal  
        pass

    def get_neighbors(self):       
        neighbors = []
        impossibles = ['a0', 'a4','c0','d0','e0','f0','f4']
        if (self.number == '0' and self.alphabet not in 'af'): 
            neighbors.extend(('b1','c1','d1','e1'))
            return neighbors
        for letter in 'abcdef':
            for number in '01234':
                if (self.isValid(self.location) == 1 and self.isAdjacent(self.location,str(letter + number)) == 1):
                    neighbors.append(str(letter + number))
        return [i for i in neighbors if i not in impossibles]

    def get_captures(self):
        captures = []
        impossibles = ['a0','a4','c0','d0','e0','f0','f4']
        for neighbors in self.get_neighbors():
            # print('DEBUG: neighbors',neighbors)
            # neighbor_neighbors = Position(neighbors[0],neighbors[1]).get_neighbors()
            if Position(neighbors[0],neighbors[1]).content() == 'O':
                neighbor_neighbors = Piece(self.location).secondAdjacent(neighbors)
                #print('DEBUG: neighbor_neighbors',neighbor_neighbors)
                if neighbor_neighbors != None:
                    if Position(neighbor_neighbors[0],neighbor_neighbors[1]).content() == ():
                        captures.append(neighbor_neighbors)              
        if len(captures) == 0:
            return None
        else:    
            return [i for i in list(set(captures)) if i not in impossibles]

class Piece(Board):

    def __init__(self, position):
        self.namePiece = 'Piece'+hex(id(self))
        self.position = position
        content = ''
        
    def adjacent(self, newposition):
        # Returns adjacent position given the adjacent position after that
        ans = None
        alph = ('a','b','c','d','e','f')
        if self.position[0] == newposition[0] or int(self.position[1]) + int(newposition[1]) - 2 == 0:
            if abs(int(self.position[1]) > int(newposition[1])) and int(newposition[1]) >= 0:
                ans = self.position[0] + str(int(newposition[1])+1) 
            elif abs(int(self.position[1]) < int(newposition[1])) and int(newposition[1])+1 <= 5:
                ans = newposition[0] + str(int(newposition[1])-1)
            else: 
                ans = None

        if self.position[1] == newposition[1]:
            if alph.index(self.position[0]) > alph.index(newposition[0]) and alph.index(newposition[0]) >= 0:
                ans =  alph[alph.index(newposition[0])+1] + newposition[1]
            elif alph.index(self.position[0]) < alph.index(newposition[0]) and alph.index(newposition[0]) <= len(alph):
                ans = alph[alph.index(newposition[0])-1] + newposition[1]
            else:
                ans = None
        if ans != None:
            if int(self.position[1]) == 0 and int(ans[1]) == 0:
                return None
            if int(ans[1]) >= 4 and ans[0] in 'af': 
                return None
        return ans

    def secondAdjacent(self, newposition):
        ans = None
        alph = ('a','b','c','d','e','f')
        
        if self.position[0] == newposition[0] or int(self.position[1]) + int(newposition[1]) - 1 == 0:
            if abs(int(self.position[1]) > int(newposition[1])) and int(newposition[1])-1 >= 0:
                ans = newposition[0] + str(int(newposition[1])-1) 
            elif abs(int(self.position[1]) < int(newposition[1])) and int(newposition[1])+1 < 5:
                ans = newposition[0] + str(int(newposition[1])+1)
            else: 
                ans = None

        elif self.position[1] == newposition[1]:
                if alph.index(self.position[0]) > alph.index(newposition[0]) and alph.index(newposition[0]) - 1 >= 0:
                    ans =  alph[alph.index(newposition[0])-1] + newposition[1]
                elif alph.index(self.position[0]) < alph.index(newposition[0]) and alph.index(newposition[0])+1 < len(alph):
                    ans = alph[alph.index(newposition[0])+1] + newposition[1]
                else:
                    ans = None
        if ans != None:
            if ans[0] in 'bcde' and int(ans[1]) == 0:
                return 'b0'
            if int(self.position[1]) == 0 and int(ans[1]) == 0:
                return None
            if (int(ans[1]) == 0 or int(ans[1]) >= 4) and ans[0] in 'af': 
                return None
        return ans

    def possibleMoves(self):
        # Generates possible positions given tiger position
        ans = []
        positions = Position(self.position[0],self.position[1]).get_neighbors()
        captures = Position(self.position[0],self.position[1]).get_captures()
        #print('DEBUG: captures ',captures)
        for i in range(len(positions)):
            # print(positions[i])
            if positions[i] in ['c0','d0','e0'] and Position(positions[i][0],positions[i][1]).content() == ():
                ans.append('b0')
            if positions[i] not in ['c0','d0','e0'] and Position(positions[i][0],positions[i][1]).content() == ():
                ans.append(positions[i])
        if captures != None :
            for i in captures:
                ans.append(i)
                # capturesPos = Piece(self.position).secondAdjacent(i)
                # if i != None or capturesPos != None:
                    # ans.append(capturesPos)
        #print('CHECK 1',list(set(ans)))            
        return list(set(ans)) #Not separated
    

    def potential_move(matrix, goatPos, movePos):
        
        matrix[[goatPos, movePos]] = matrix[[movePos, goatPos]]

        return Goat.testCostFunction(matrix)

    def testCostFunction(Matr):

        weightDict = {}

        #Hardcoded dictionary that shows all adjacent positions (one way)
        #Potential To Do: Work on using both ways for cost function IE Check 0,2 and 2,0 (Might not matter if using trioList)
        #Are lists better?
        adjList = {0: [0, 2], 1: [0, 3], 2: [0, 4], 3: [0, 5], 4: [1, 2], 5: [2, 3], 6: [3, 4], 7: [4, 5], 8: [5, 6], 9: [1, 7], 10: [2, 8], 
                  11: [3, 9], 12: [4, 10], 13: [5, 11], 14: [6, 12], 15: [7, 8], 16: [8, 9], 17: [9, 10], 18: [10, 11], 19: [11, 12], 20: [7, 13], 
                  21: [8, 14], 22: [9, 15], 23: [10, 16], 24: [11, 17], 25: [12, 18], 26: [13, 14], 27: [14, 15], 28: [15, 16], 29: [16, 17], 30: [17, 18], 
                  31: [14, 19], 32: [15, 20], 33: [16, 21], 34: [17, 22], 35: [19, 20], 36: [20, 21], 37: [21, 22]}

        #Hardcoded list that shows all possible trio positions (one way)
        #To Do: In cost function find a way to check backwards IE 0,2,8 and 8,2,0 one way may change more
        trioList = [[0, 2, 8], [0, 3, 9], [0, 4, 10], [0, 5, 11], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12], 
                    [13, 14, 15], [14, 15, 16], [15, 16, 17], [16, 17, 18], [1, 7, 13], [6, 12, 18], [2, 8, 14], [8, 14, 19], [3, 9, 15], [9, 15, 20], [4, 10, 16], 
                    [10, 16, 21], [5, 11, 17], [11, 17, 22], [19, 20, 21], [20, 21, 22]]
        
        #Hardcoded list that shows all positions on the board on the edge (Not used)
        edgeList = [0,1,6,7,12,13,18,19,20,21,22]
        #Hardcoded list for middle or body positions (Not used)
        bodyList = [2,3,4,5,8,9,10,11,14,15,16,17]

        cost = 0

        #Extra matrices that we can manipulate
        trioTest = Matr.copy()
        MatrB = Matr.copy()

        #Possible single position cost function
        #Ideas: Are edge positions stronger or body positions? For what pieces?
        #Notes: Have the empty space have more weight because if a goat is eaten that will affect the cost in a bad way (It will say a goat getting eaten is a good thing (ITS NOT))
        
        #for x in range(0,23):
            #if ((Matr[x] == [0,0,1]).all()):
            #    cost += 5 
            #if ((Matr[x] == [0,1,0]).all()):
            #    cost += 3
            #Corners only
            #if (x in corner_vals and (Matr[x] == [1,0,0]).all()): #if tiger in corner
            #    cost -= 5

        #End of single position cost function

        #Start of two positions cost function
        #Ideas:
        #Notes:
        Matr = Matr.reshape(23,3,1,1)
        MatrT = np.transpose(Matr)

        Matr = Matr*MatrT   #Create 23x3x3x23 matrix

        #Vectors for each piece
        T = [1,0,0] 
        G = [0,1,0]
        E = [0,0,1]
        
        for x in range(0,38):

            #This is a single pos cost function inside the pair loop to reduce amount of loops?
            if x <= 22:
                if   ((MatrB[x] == [0,0,1]).all()): #If space is empty
                    cost += 5 
                elif ((MatrB[x] == [0,1,0]).all()): #If space has goat
                    cost += 3
                elif (x in edgeList and (MatrB[x] == [1,0,0]).all()): #if tiger in edge pos
                    cost -= 5
            #End of single pos cost function

            #Go through all adj positions in 23x3x3x23 matrix and compare it to a specific pair of pieces adjust cost 
            if  ((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(T,G)).all()):
                cost += 5
            elif((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(G,G)).all()):
                cost += 5
            elif((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(G,E)).all()):
                cost += 5
            elif((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(E,E)).all()):
                cost += 5
            elif((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(T,T)).all()):
                cost += 5
            elif((Matr[adjList[x][0],:,:,adjList[x][1]] == np.outer(T,E)).all()):
                cost += 5

        #End of two position cost function

        #Start of trio position cost function
        #Ideas:
        #Notes:

        #Get list of all trios replace all positions with their pieces
        trioListPiece = trioList.copy()
        for y in trioListPiece:
            for b in range(0,3):
                val = trioTest[y[b]]
                if (val == [1,0,0]).all():
                    y[b] = 'T'
                elif (val == [0,1,0]).all():
                    y[b] = 'G'
                elif (val == [0,0,1]).all():
                    y[b] = 'E'

        for x in trioListPiece:
            if(x == ['T','G','E']):
                cost += 5
            elif(x == ['E','G','T']):
                cost += 5
            elif(x == ['T','G','T']):
                cost -= 5
            elif(x == ['G','G','T']):
                cost -= 7
            elif(x == ['T','E','T']):
                cost -= 5
            elif(x == ['T','G','G']):  
                cost -= 7

        #End of trio position cost function

        return cost
    
class Tiger(Piece):
    def place(self):
        #print('Piece ',self.namePiece)
        if Position(self.position[0],self.position[1]).content() == (): 
           Position(self.position[0],self.position[1]).place('X')
        pass 

    def move(self,newposition):
        if Position(self.position[0],self.position[1]).content() == 'X' and Position(newposition[0],newposition[1]).content() == ():
            Position(newposition[0],newposition[1]).place('X')
            Position(self.position[0],self.position[1]).place(())
        else:
            print('DEBUG: Tiger cannot go there')
            return -1 
        return 1

    def capture(self,newposition):
        new = self.adjacent(newposition)
        if new == self.position or new == None or Position(self.position[0],self.position[1]).get_captures() == None:
            return -1
        # print('DEBUG: Position(self.position[0],self.position[1]).get_captures() ',Position(self.position[0],self.position[1]).get_captures())
        if new not in Position(self.position[0],self.position[1]).get_captures() and Position(self.position[0],self.position[1]).content() == 'X' and Position(newposition[0],newposition[1]).content() != ():
            print('DEBUG: error on capture')
            return -1
        Position(self.position[0],self.position[1]).place(())
        Position(new[0],new[1]).place(())
        
        new = self.adjacent(newposition)
        Position(newposition[0],newposition[1]).place('X')
        return 1
    


class Goat(Piece):
    inplay = 0
        
    def move(self,newposition):
        # print('DEBUG: self.position ',self.position)
        # print('DEBUG: newposition ', newposition)
        if Position(self.position[0],self.position[1]).content() == 'O' and Position(newposition[0],newposition[1]).content() == ():
            Position(newposition[0],newposition[1]).place('O')   
            Position(self.position[0],self.position[1]).place(())
        else:
            print("Goat cannot go there")
            return -1
        return 1

    def place(self):
        if Position(self.position[0],self.position[1]).content() == (): 
            Position(self.position[0],self.position[1]).place('O')
        pass 

if __name__ == "__main__":
    from functions import *
    # Game Flow
    Board().clearBoard()
    Tiger('a1').place()
    Tiger('c1').place()
    Tiger('d1').place()
    Goat('e1').place()
    # Goat('c1').place()
    # Goat('e1').place()
    #Board().printBoard()

    # print(Tiger('d1').secondA())  
    # print(Position('d','1').get_captures())
    # print(Tiger('f1').possibleMoves())
    #Board().printBoard()
    
    #print(Piece('a1').secondAdjacent('a2'))
