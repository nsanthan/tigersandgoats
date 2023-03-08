'''
Huligutta (Goats and Tigers)
file: game.py
Description: GUI of the game using TKinter
'''

__author__ = "Clyde James Felix"
__email__ = "cjfelix.hawaii.edu"
__status__ = "Dev"

import time
from tkinter import *
from tkinter import messagebox
import os
import numpy as np
import sys
from huligutta import *
from functions import *
from PIL import ImageTk, Image
from random import randint, choice

# Board parts
numPosition = 23 
boardSize = 500

Board().clearBoard()

# Game modes:
#   

class Main():

    def __init__(self,mode):
        # For self.turn (is it the computer's turn?) 
        self.turn = False
        # self.move is used when a piece is used to move from one location to another. True
        # if a piece is currently under move (ie, a piece has been clicked, and is not yet 
        # transferred somewhere else
        self.move = False 


        try:
            tiger_img = Image.open('./images/tiger-512.png')
            tiger_img =tiger_img.resize((30,30),Image.ANTIALIAS)
            goat_img = Image.open('./images/goat.png')
            goat_img =goat_img.resize((30,30),Image.ANTIALIAS)    
        except:
            print('Problem loading the images')

        self.window = Tk()        
        self.window.title('Huligutta (Goats & Tigers)')
        self.window.geometry('500x500')
        self.window.resizable(0,0)
        # self.window.tk_focusFollowsMouse()
        # self.window.tk.call('tk', 'scaling', 17)
        self.tiger = ImageTk.PhotoImage(tiger_img)
        self.goat = ImageTk.PhotoImage(goat_img)
        self.empty = ImageTk.PhotoImage(file='./images/empty.png') 
        self.canvas = Canvas(self.window,width=boardSize,height=boardSize)
        self.initialize_board()

        self.canvas.pack()
        self.location = ''
        self.turntext = StringVar()
        self.numGoats = StringVar()
        self.goatsEatentext = StringVar()
        self.selectedBtn = StringVar()

        # Number of goats eaten
        self.goatEaten = 0
        # Number of goats placed thus far (regardless of whether they are still on board or not)
        self.goatCount = 0
        self.moveCount = 0
        self.moveCount_prev = 0

        self.turnDisp = Label(self.window, font=("Helvetica", 16), textvariable=self.turntext).place(x=boardSize - 100,y= 30)
        self.selectedDisp = Label(self.window, font=("Helvetica", 16), textvariable=self.selectedBtn).place(x=boardSize - 100,y= boardSize - 30)
        self.goatDisp = Label(self.window, font=("Helvetica", 16), textvariable=self.numGoats).place(x=10,y= 30)
        self.goatEatenDisp = Label(self.window, font=("Helvetica", 16), textvariable=self.goatsEatentext).place(x= 10,y= 50)
        self.numGoats.set("Number of goats: " + str(self.goatCount))
        self.goatsEatentext.set("Goats eaten: " + str(self.goatEaten))
        self.turnDisplay()
        self.selectedToggle()

        # Buttons
        self.btn1  = Button(self.window, image=self.empty, command=lambda : self.button_position('b0')).place(x=boardSize/2,y=boardSize/10,height=30,width=30,anchor=CENTER)
        self.btn2  = Button(self.window, image=self.empty, command=lambda : self.button_position('a1')).place(x=boardSize/10,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn3  = Button(self.window, image=self.empty, command=lambda : self.button_position('a2')).place(x=boardSize/10,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn4  = Button(self.window, image=self.empty, command=lambda : self.button_position('a3')).place(x=boardSize/10,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        self.btn5  = Button(self.window, image=self.empty, command=lambda : self.button_position('b1')).place(x=boardSize/2 - 65,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn6  = Button(self.window, image=self.empty, command=lambda : self.button_position('b2')).place(x=boardSize/2- 100,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn7  = Button(self.window, image=self.empty, command=lambda : self.button_position('b3')).place(x=boardSize/2-135,y=boardSize/2+70,height=30,width=30,anchor=CENTER)
        self.btn8  = Button(self.window, image=self.empty, command=lambda : self.button_position('b4')).place(x=boardSize/10,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)
        self.btn9  = Button(self.window, image=self.empty, command=lambda : self.button_position('c1')).place(x=boardSize/2 - 25,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn10 = Button(self.window, image=self.empty, command=lambda : self.button_position('c2')).place(x=boardSize/2 - 38,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn11 = Button(self.window, image=self.empty, command=lambda : self.button_position('c3')).place(x=boardSize/2 - 53,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        self.btn12 = Button(self.window, image=self.empty, command=lambda : self.button_position('c4')).place(x= boardSize/2 - 80,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)
        self.btn13 = Button(self.window, image=self.empty, command=lambda : self.button_position('d1')).place(x=boardSize/2 + 25,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn14 = Button(self.window, image=self.empty, command=lambda : self.button_position('d2')).place(x=boardSize/2 + 38,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn15 = Button(self.window, image=self.empty, command=lambda : self.button_position('d3')).place(x=boardSize/2 + 53,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        self.btn16 = Button(self.window, image=self.empty, command=lambda : self.button_position('d4')).place(x=boardSize/2 + 80,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)
        self.btn17 = Button(self.window, image=self.empty, command=lambda : self.button_position('e1')).place(x=boardSize/2 + 65,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn18 = Button(self.window, image=self.tiger, command=lambda : self.button_position('e2')).place(x=boardSize/2+100,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn19 = Button(self.window, image=self.empty, command=lambda : self.button_position('e3')).place(x=boardSize/2 + 135,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        self.btn20 = Button(self.window, image=self.empty, command=lambda : self.button_position('e4')).place(x=boardSize - boardSize/10,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)        
        self.btn21 = Button(self.window, image=self.empty, command=lambda : self.button_position('f1')).place(x=boardSize-boardSize/10,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        self.btn22 = Button(self.window, image=self.empty, command=lambda : self.button_position('f2')).place(x=boardSize-boardSize/10,y=boardSize/2,height=30,width=30,anchor=CENTER)
        self.btn23 = Button(self.window, image=self.empty, command=lambda : self.button_position('f3')).place(x=boardSize-boardSize/10,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)

    def initialize_board(self):
        # Draws the board
        self.canvas.create_rectangle(boardSize/10,boardSize/2 - 70,boardSize-boardSize/10,boardSize/2+70)    
        self.canvas.create_line(boardSize/10,boardSize/2,boardSize-boardSize/10,boardSize/2)
        self.canvas.create_line(boardSize/2,boardSize/10, boardSize/10,boardSize - boardSize/10)
        self.canvas.create_line(boardSize/2,boardSize/10, boardSize - boardSize/10,boardSize - boardSize/10)
        self.canvas.create_line(boardSize/10,boardSize - boardSize/10,boardSize - boardSize/10,boardSize - boardSize/10)
        self.canvas.create_line(boardSize/2,boardSize/10, boardSize/2 - 80,boardSize - boardSize/10)
        self.canvas.create_line(boardSize/2,boardSize/10, boardSize/2 + 80,boardSize - boardSize/10)

        printAndLog('========================')
        attempts = textCount('Attempts: ')
        printAndLog('Attempts: ' +  str(attempts))
        printAndLog('Game Mode: '+ mode)
        printAndLog('========================')

    def button_position(self,pos):
        
        # Called whenever a button is clicked. pos is the location of the  
        # button clicked. For example, if button b0 is clicked, it calls button_position(self,'b0').

        self.moveCount_prev = self.moveCount

        if mode == 'pvp':
            self.pvpMode(pos)
        elif mode == 'goatPlayer':
            self.goatMode(pos)
        elif mode == 'tigerPlayer':
            self.tigerMode(pos)    
        elif mode == 'ai_vs_ai':
            self.ai_vs_aiMode(pos)     

        if self.moveCount_prev != self.moveCount:
            self.update()
            self.collectData()
        self.window.mainloop()                

    def pvpMode(self,pos):
        # How goats move
        if self.turn == False:
            if self.boardPosition.get(pos[0]+pos[1]).content() == 'X':
                print('You must select any empty or goat positions')
            elif Position(pos[0],pos[1]).content() == () and self.move == False:
                if self.goatCount < 15:
                    Goat(pos).place()
                    self.turn = True
                else: 
                    print("exceeded goats amount")
            elif Position(pos[0],pos[1]).content() == 'O':
                print('self.move ',self.move)
                if self.goatCount == 15:
                    if pos == self.location:
                        self.move = not self.move
                # Select valid position to move
                    elif self.move == False: 
                        self.move = True
                        self.location = pos
                else:
                    print("Goats can only be moved if 15 goats are placed")
            else:
                
                if Goat(self.location).move(pos) == 1:
                    self.move = False
                    self.location = ''
                    self.turn = True
                    self.moveCount = self.moveCount + 1
            pass

        # How tigers move
        elif self.turn == True:
            
            # print('DEBUG: possible moves',Piece(pos).possibleMoves())
            if Position(pos[0],pos[1]).content() != 'X' and self.move == False:
                print('You must select any current tiger positions') 

            elif Position(pos[0],pos[1]).content() == 'X':
                if pos == self.location:
                    self.move = not self.move
                elif self.location == '' or self.move == False or pos != self.location:
                    self.move = True
                    self.location = pos

            elif Position(pos[0],pos[1]).content() == () and self.move == True:
                # print('DEBUG: location',self.location)
                # print('DEBUG: secondAdjacent',Piece(self.location).secondAdjacent(pos))
                # print('DEBUG: Adjacent',Piece(self.location).adjacent(pos))
                print('DEBUG: possiblemoves 2 ', Piece(self.location).possibleMoves())
                if pos in Position(self.location[0],self.location[1]).get_neighbors():
                    tigerMoveFlag = Tiger(self.location).move(pos) 

                    if tigerMoveFlag == 1:
                        self.move = False
                        self.location = ''
                        self.turn = False
                        self.moveCount = self.moveCount + 1
                        return

                elif pos in Piece(self.location).possibleMoves():
                    if Tiger(self.location).capture(pos) == 1:

                        self.goatEaten = self.goatEaten + 1 
                        self.move = False
                        self.location = ''
                        self.turn = False
                        self.moveCount = self.moveCount + 1

                else:
                    print('Error on capture')
                    self.move = False
                    self.location = ''
                    self.turn = True

    def goatMode(self,pos):
#        button_position(self,pos)
        if self.turn == False:
            if Position(pos[0],pos[1]).content() == 'X':
                print('You must select any empty or goat positions')
            elif Position(pos[0],pos[1]).content() == ():
                if self.move == False:
                    if self.goatCount < 15:
                        Goat(pos).place()
                        self.turn = True
                    else: 
                        print("All 15 goats placed already")
                if self.move == True:
                    if Goat(self.location).move(pos) == 1:
                        # should enter this line if it is a valid move
                        self.turn = True
                        self.move = False
                        self.location = ''
                    else:
                        print('Invalid move, try again')
            elif Position(pos[0],pos[1]).content() == 'O':
                if self.goatCount == 15:
                    if self.move == True:
                        if pos == self.location:
                            # perhaps unnecessary, combine this with else. 
                            # self.location was old place if non-empty, pos is the button clicked
                            # equality means clicked on the same piece twice, just ignore and reset 
                            self.turn = False
                            self.move = False
                            self.location = ''
                        else:
                            # trying to place a goat on another goat. Invalid move, just ignore and reset
                            if Goat(self.location).move(pos) == 1:
                                print('Something is majorly wrong!!')
                            print('Invalid move attempted from ',self.location,' to ',pos,'. Try again.')
                            self.turn = False
                            self.move = False
                            self.location = ''
                    else:
                        # this now selects a goat piece to move. save old position, indicate movement
                        self.move = True
                        self.location = pos
                else:
                    print("Goats can only be moved after all 15 goats are placed")
                    
        if self.turn == True:
            # pause for a bit to ensure player sees the goat placement
            # time.sleep(1)
            # Randomize tiger choice
            numTigers = 3
            possibleCaptures = {}
            tigers = tigerPositions(Board().boardPositions)

            # figure out all possible capture positions
            for tiger in tigers:
                if Position(tiger[0],tiger[1]).get_captures() != None:
                    for capture in Position(tiger[0],tiger[1]).get_captures():
                        possibleCaptures[tiger] = capture
            print(possibleCaptures)

            # chooses one of the tigers
            tigerPos = choice(tigers)
        
            # ignore all tigers with no moves  
            while len(Tiger(tigerPos).possibleMoves()) == 0:
                tigers.remove(tigerPos)
                if len(tigers) == 0:
                    # at this point, the tigers have lost. Reset everything so that
                    # update() can figure out who won.
                    print("Tigers have lost")
                    self.move = False
                    self.location = ''
                    self.moveCount = self.moveCount+1
                    self.turn = False
                    return
                else:
                    tigerPos = choice(tigers)
                if Position(tigerPos[0],tigerPos[1]).get_captures() != None:
                    # if a tiger has a capture move, no need to look further
                    # this seems to be a spurious line, will never hit here
                    print('PRASADDEBUG: How did I get here?', tigerPos)
                    break
                
            tigerChoice = choice(Tiger(tigerPos).possibleMoves())
            if pos in tigerPos:
                #PRASADDEBUG: this should not be there as well
                del tigerChoice[tigerChoice.index(pos)]


            if len(possibleCaptures) != 0:
                tigerPos,where2go = choice(list(possibleCaptures.items()))
                # print('DEBUG possibleMOves', tigerPos,' ',where2go)
                # print('DEBUG TIGERCPOS', tigerPos)
                if Tiger(tigerPos).capture(where2go) == 1:
                    print('Possible Captures: ', possibleCaptures, 'Actual: ',tigerPos, where2go)
                    self.goatEaten = self.goatEaten + 1
                    self.move = False
                    self.location = ''
                    self.turn = False
                    self.moveCount = self.moveCount + 1
            elif tigerChoice in Position(tigerPos[0],tigerPos[1]).get_neighbors():
                tigerMoveFlag = Tiger(tigerPos).move(tigerChoice) 
                if tigerMoveFlag == 1:
                    print('Tiger from', tigerPos, ' to ', tigerChoice)
                    self.move = False
                    self.turn = False
                    self.moveCount = self.moveCount + 1
                    return
            else:
                # should never get here
                print('Error on capture')
                self.move = False
                self.location = ''
                self.turn = True

    def tigerMode(self,pos):

        if self.turn == True:
            # print('DEBUG: possible moves',Piece(pos).possibleMoves())
            if Position(pos[0],pos[1]).content() != 'X' and self.move == False:
                print('You must select any current tiger positions') 

            elif Position(pos[0],pos[1]).content() == 'X':
                if pos == self.location:
                    self.move = not self.move
                elif self.location == '' or self.move == False or pos != self.location:
                    self.move = True
                    self.location = pos

            elif Position(pos[0],pos[1]).content() == () and self.move == True:
                # print('DEBUG: location',self.location)
                # print('DEBUG: secondAdjacent',Piece(self.location).secondAdjacent(pos))
                # print('DEBUG: Adjacent',Piece(self.location).adjacent(pos))
                # print('DEBUG: possiblemoves 2 ', Piece(self.location).possibleMoves())
                if pos in Position(self.location[0],self.location[1]).get_neighbors():
                    tigerMoveFlag = Tiger(self.location).move(pos) 

                    if tigerMoveFlag == 1:
                        self.move = False
                        self.location = ''
                        self.turn = False
                        self.moveCount = self.moveCount + 1
                        
                elif pos in Piece(self.location).possibleMoves():
                    if Tiger(self.location).capture(pos) == 1:

                        self.goatEaten = self.goatEaten + 1 
                        self.move = False
                        self.location = ''
                        self.turn = False
                        self.moveCount = self.moveCount + 1

                else:
                    print('Error on capture')
                    self.move = False
                    self.location = ''
                    self.turn = True       
        
        if self.turn == False:
           # Randomize goat positions
            emptyPos = emptyPositions(Board().boardPosition)
            goats = goatPositions(Board().boardPosition)
            # print("DEBUG: goats ", goats)

            if self.goatCount == 15:
                goatPos = choice(goats)

                while len(Goat(goatPos).possibleMoves()) == 0:
                    if len(goats) != 0:
                        goats.remove(goatPos)
                    else:
                        return

                goatChoice = choice(Goat(goatPos).possibleMoves())
                # print('DEBUG goatChoice ',goatChoice)

                if pos in goatPos:
                    del goatChoice[goatChoice.index(pos)]

                # print('###### Debug ######')
                # print('goat to move:', goatPos)
                # print('Possible moves: ', Goat(goatPos).possibleMoves())
                # print('Choice the goat made: ',choice(Goat(goatPos).possibleMoves()))

                if goatChoice in Position(goatPos[0],goatPos[1]).get_neighbors():
                    goatMoveFlag = Goat(goatPos).move(goatChoice) 

                    if goatMoveFlag == 1:
                        self.move = False
                        self.turn = True
                        self.moveCount = self.moveCount + 1
                        return

                else:
                    print('Error')
                    self.move = False
                    self.location = ''
                    self.turn = False
            else:
                goatChoice = choice(emptyPos)
                Goat(goatChoice).place()
                self.move = False
                self.turn = True

                
    def ai_vs_aiMode(self,pos):

       if self.turn == False:
            emptyPos = emptyPositions(Board().boardPositions)
            goats = goatPositions(Board().boardPositions)

            if self.goatCount == 15:
                goatPos = choice(goats)

                while len(Goat(goatPos).possibleMoves()) == 0:
                    if len(goats) != 0:
                        goats.remove(goatPos)
                    else:
                        return

                goatChoice = choice(Goat(goatPos).possibleMoves())

                if pos in goatPos:
                    del goatChoice[goatChoice.index(pos)]

                if goatChoice in Position(goatPos[0],goatPos[1]).get_neighbors():
                    goatMoveFlag = Goat(goatPos).move(goatChoice) 

                    if goatMoveFlag == 1:
                        self.move = False
                        self.turn = True
                        self.moveCount = self.moveCount + 1
                        return

                else:
                    print('Error')
                    self.move = False
                    self.location = ''
                    self.turn = False
            else:
                goatChoice = choice(emptyPos)
                Goat(goatChoice).place()
                self.move = False
                self.turn = True

       if self.turn == True:
            numTigers = 3
            possibleCaptures = {}
            tigers = tigerPositions(Board().boardPositions)

            for tiger in tigers:
                if Position(tiger[0],tiger[1]).get_captures() != None:
                    for capture in Position(tiger[0],tiger[1]).get_captures():
                        possibleCaptures[tiger] = capture
            print(possibleCaptures)

            tigerPos = choice(tigers)
        
            while len(Tiger(tigerPos).possibleMoves()) == 0:
                tigers.remove(tigerPos)
                if len(tigers) == 0:
                    print("Tigers have lost")
                    self.move = False
                    self.location = ''
                    self.moveCount = self.moveCount+1
                    self.turn = False
                    return
                else:
                    tigerPos = choice(tigers)
                if Position(tigerPos[0],tigerPos[1]).get_captures() != None:
                    print('PRASADDEBUG: How did I get here?', tigerPos)
                    break
                
            tigerChoice = choice(Tiger(tigerPos).possibleMoves())
            if pos in tigerPos:
                del tigerChoice[tigerChoice.index(pos)]

            if len(possibleCaptures) != 0:
                tigerPos,where2go = choice(list(possibleCaptures.items()))
                if Tiger(tigerPos).capture(where2go) == 1:
                    print('Possible Captures: ', possibleCaptures, 'Actual: ',tigerPos, where2go)
                    self.goatEaten = self.goatEaten + 1
                    self.move = False
                    self.location = ''
                    self.turn = False
                    self.moveCount = self.moveCount + 1
            elif tigerChoice in Position(tigerPos[0],tigerPos[1]).get_neighbors():
                tigerMoveFlag = Tiger(tigerPos).move(tigerChoice) 
                if tigerMoveFlag == 1:
                    print('Tiger from', tigerPos, ' to ', tigerChoice)
                    self.move = False
                    self.turn = False
                    self.moveCount = self.moveCount + 1
                    return
            else:
                print('Error on capture')
                self.move = False
                self.location = ''
                self.turn = True

    def update(self):
        # Updates the Screen
        possible_pos = ['a1','a2','a3','b0','b1','b2','b3','b4','c1','c2','c3','c4','d1','d2','d3','d4','e1','e2','e3','e4','f1','f2','f3']
        numGoats = 0

        tigerPos = tigerPositions(Board().boardPositions)
        possibleMovesCount = 0
        for i in range(len(possible_pos)):
            if Position(possible_pos[i][0],possible_pos[i][1]).content() == ():
                self.change_button(possible_pos[i],self.empty)
            elif Position(possible_pos[i][0],possible_pos[i][1]).content() == 'O':
                numGoats = numGoats + 1
                self.change_button(possible_pos[i],self.goat)
            else:
                self.change_button(possible_pos[i],self.tiger)
        
        for tiger in tigerPos:
            possibleMovesCount = possibleMovesCount + len(Piece(tiger).possibleMoves())


        self.goatCount = numGoats+self.goatEaten
        self.numGoats.set("Goats placed: " + str(self.goatCount))
        self.goatsEatentext.set("Goats eaten: " + str(self.goatEaten))
        self.turnDisplay()
        self.selectedToggle()

        # Endgame
        if possibleMovesCount == 0:
            messagebox.showinfo("Game Over: Goat wins") 
            return

        if self.goatEaten == 5:
            messagebox.showinfo("Game Over: Tiger wins") 
            return

    def collectData(self):
        printAndLog("Move: " + str(self.moveCount))
        printAndLog("--------------------")
        printAndLog("Goats: " + str(self.goatCount))
        tigers = tigerPositions(Board().boardPositions)
        printAndLog("Tigers positions: " + str(tigers))
        printAndLog(str(Board().boardPositions))
        editDistance = edit_distance(Board().boardPositions)
        printAndLog("Edit distance: " + str(editDistance))
        
    def selectedToggle(self):
        if self.move == True:
            self.selectedBtn.set('Selected')
        else:
            self.selectedBtn.set('')

    def turnDisplay(self):
        # Displays turn as text in the window
        if self.turn:
            self.turntext.set("Turn: Tiger")
        else:
            self.turntext.set("Turn: Goat")

    def change_button(self,pos,img):
        # change the images of the board pieces

        if pos == 'b0':
            self.btn1 = Button(self.window, image=img, command=lambda : self.button_position('b0')).place(x=boardSize/2,y=boardSize/10,height=30,width=30,anchor=CENTER)
        if pos == 'a1':
            self.btn2 = Button(self.window, image=img, command=lambda : self.button_position('a1')).place(x=boardSize/10,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        if pos == 'a2':
            self.btn3 = Button(self.window, image=img, command=lambda : self.button_position('a2')).place(x=boardSize/10,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'a3':
            self.btn4 = Button(self.window, image=img, command=lambda : self.button_position('a3')).place(x=boardSize/10,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        if pos == 'b1':
            self.btn5 = Button(self.window, image=img, command=lambda : self.button_position('b1')).place(x=boardSize/2 - 65,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)  
        if pos == 'b2':
            self.btn6 = Button(self.window, image=img, command=lambda : self.button_position('b2')).place(x=boardSize/2- 100,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'b3':
            self.btn7 = Button(self.window, image=img, command=lambda : self.button_position('b3')).place(x=boardSize/2-135,y=boardSize/2+70,height=30,width=30,anchor=CENTER)
        if pos == 'b4':
            self.btn8 = Button(self.window, image=img, command=lambda : self.button_position('b4')).place(x=boardSize/10,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER) 
        if pos == 'c1':
            self.btn9 = Button(self.window, image=img, command=lambda : self.button_position('c1')).place(x=boardSize/2 - 25,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        if pos == 'c2':
            self.btn10 = Button(self.window, image=img, command=lambda : self.button_position('c2')).place(x=boardSize/2 - 38,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'c3':        
            self.btn11 = Button(self.window, image=img, command=lambda : self.button_position('c3')).place(x=boardSize/2 - 53,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        if pos == 'c4':
            self.btn12 = Button(self.window, image=img, command=lambda : self.button_position('c4')).place(x= boardSize/2 - 80,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)
        if pos == 'd1':     
            self.btn13 = Button(self.window, image=img, command=lambda : self.button_position('d1')).place(x=boardSize/2 + 25,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        if pos == 'd2':
            self.btn14 = Button(self.window, image=img, command=lambda : self.button_position('d2')).place(x=boardSize/2 + 38,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'd3':      
            self.btn15 = Button(self.window, image=img, command=lambda : self.button_position('d3')).place(x=boardSize/2 + 53,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        if pos == 'd4':
            self.btn16 = Button(self.window, image=img, command=lambda : self.button_position('d4')).place(x=boardSize/2 + 80,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)  
        if pos == 'e1':  
            self.btn17 = Button(self.window, image=img, command=lambda : self.button_position('e1')).place(x=boardSize/2 + 65,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        if pos == 'e2':
            self.btn18 = Button(self.window, image=img, command=lambda : self.button_position('e2')).place(x=boardSize/2+100,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'e3':
            self.btn19 = Button(self.window, image=img, command=lambda : self.button_position('e3')).place(x=boardSize/2 + 135,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)
        if pos == 'e4':
            self.btn20 = Button(self.window, image=img, command=lambda : self.button_position('e4')).place(x=boardSize - boardSize/10,y=boardSize - boardSize/10,height=30,width=30,anchor=CENTER)        
        if pos == 'f1':
            self.btn21 = Button(self.window, image=img, command=lambda : self.button_position('f1')).place(x=boardSize-boardSize/10,y=boardSize/2 - 70,height=30,width=30,anchor=CENTER)
        if pos == 'f2':
            self.btn22 = Button(self.window, image=img, command=lambda : self.button_position('f2')).place(x=boardSize-boardSize/10,y=boardSize/2,height=30,width=30,anchor=CENTER)
        if pos == 'f3': 
            self.btn23 = Button(self.window, image=img, command=lambda : self.button_position('f3')).place(x=boardSize-boardSize/10,y=boardSize/2 + 70,height=30,width=30,anchor=CENTER)

    def start(self):
        # Sets up the game window
        # Tiger's initial positions
        Tiger('b0').place()
        Tiger('c1').place()
        Tiger('d1').place()

        if mode == 'tigerPlayer':
            goats = goatPositions(Board().boardPositions)
            empty = emptyPositions(Board().boardPositions)
            emptyPos = choice(empty)
            Goat(emptyPos).place()
            self.turn = True
        self.update()
        self.window.mainloop()        

if __name__ == "__main__":
    
    # mode = 'pvp'          # Player vs. Player
    # mode = 'ai_vs_ai'     # ai vs ai
    mode = 'goatPlayer'   # Human player is Goat, computer plays Tiger
    # mode = 'tigerPlayer'  # Human player is Tiger, computer plays Goat

    game = Main(mode)
    game.start()
