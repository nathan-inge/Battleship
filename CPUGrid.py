import myturtle
import random
from Grid import *
import tkinter as tk
class CPUGrid(Grid):
    def __init__(self,size = 10):
        self.size = size
        root = tk.Tk()
        self.screen_height = int(root.winfo_screenheight())
        
        self.scalar = self.screen_height//(self.size*4)
        self.fontSize = self.scalar//2
        self.t = myturtle.Turtle()
        self.s = myturtle.Screen()
        self.shipLocations = []
        self.numShips = self.size//3
        self.correctGuesses = []
        self.wrongGuesses = []

    def guess(self):
        okGuess = False
        while(okGuess == False):
            if len(self.correctGuesses)%3 == 0:
                x = random.randrange(1,self.size+1)
                y = random.randrange(1,self.size+1)
            else:
                lastHit = self.correctGuesses[-1]
                lastX = lastHit[0]
                lastY = lastHit[1]
                xORy = random.randrange(0,5)
                if xORy == 0:
                    lastX += 1
                elif xORy == 1:
                    lastY += 1
                elif xORy == 2:
                    lastX -= 1
                else:
                    lastY -= 1
                x = lastX
                y = lastY

            if x > self.size or y > self.size or x < 1 or y < 1:
                continue
            elif (x,y) in self.correctGuesses:
                continue
            elif (x,y) in self.wrongGuesses:
                continue
            else:
                break      
            
        
        
        if (x,y) in self.shipLocations:
            self.markHit(x,y)
            self.correctGuesses.append((x,y))
            return True
        else:
            self.markMiss(x,y)
            self.wrongGuesses.append((x,y))
            return False

    def drawGrid(self):
        self.screen_height -= int(self.screen_height * .1)      
        self.s.setup(self.screen_height/2,self.screen_height/2,-1,-1)

        
        #self.s.bgcolor('gray')
        self.s.title('BATTLESHIP - CPU')
        totLen = (self.size * self.scalar) + self.scalar
        self.s.setworldcoordinates(-self.scalar,-self.scalar,totLen,totLen)
        self.t.speed(0)
        self.t.hideturtle()
        def drawSquare(t,sideLen):
            for i in range(4):
                t.forward(sideLen)
                t.left(90)
        for bottomRow in range(self.size):
            self.t.up()
            self.t.setposition((bottomRow*self.scalar)+(self.scalar/3),-(self.scalar/1.5))
            self.t.write(str(bottomRow+1),font = ('Arial',self.fontSize, 'normal'))
        for row in range(self.size):
            self.t.up()            
            self.t.setposition(0,row*self.scalar)
            self.t.down()
            for column in range(self.size):
                drawSquare(self.t,self.scalar)
                self.t.forward(self.scalar)
            self.t.up()
            self.t.setposition(-(self.scalar/2),(row*self.scalar)+(self.scalar/3))
            self.t.write(str(row+1),font = ('Arial',self.fontSize, 'normal'))  
        self.s.listen()

        
    def getCorrectGuesses(self):
        return self.correctGuesses

    def getWrongGuesses(self):
        return self.wrongGuesses




        
