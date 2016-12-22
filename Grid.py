import cTurtle
import random
class Grid:
    def __init__(self,size = 10, scalar = 50):
        self.size = size
        self.scalar = scalar
        self.fontSize = self.scalar//3
        self.t = cTurtle.Turtle()
        self.shipLocations = []
        self.numShips = self.size//3

    def setScreen(self):
        totLen = (self.size * self.scalar) + self.scalar
        self.t.setWorldCoordinates(-self.scalar,-self.scalar,totLen,totLen)
        self.t.setposition(0,0)    
                
    def drawGrid(self):
        self.t.speed(0)
        self.t.hideturtle()
        def drawSquare(t,sideLen):
            for i in range(4):
                t.forward(sideLen)
                t.left(90)
        for bottomRow in range(self.size):
            self.t.up()
            self.t.setposition((bottomRow*self.scalar)+(self.scalar/3),-(self.scalar/2))
            self.t.write(str(bottomRow+1),font = ('Arial',self.fontSize, 'normal'))
        for row in range(self.size):
            self.t.up()            
            self.t.setposition(0,row*self.scalar)
            self.t.down()
            for column in range(self.size):
                drawSquare(self.t,self.scalar)
                self.t.forward(self.scalar)
            self.t.up()
            self.t.setposition(-(self.scalar/3),(row*self.scalar)+(self.scalar/3))
            self.t.write(str(row+1),font = ('Arial',self.fontSize, 'normal'))   


    def writeTitle(self,title):
        self.t.up()
        self.t.setposition((self.size//3)*self.scalar,(self.size*self.scalar)+(self.scalar/3))
        self.t.write(title,font = ('Arial',self.fontSize, 'normal'))
            

    def markHit(self,x,y,color = 'green'):
        self.t.up()
        scaledX = (self.scalar/2)+ (self.scalar*(x-1))
        scaledY = (self.scalar/2)+ (self.scalar*(y-1))
        self.t.setposition(scaledX,scaledY)
        self.t.dot(self.scalar*(2/3),color)

    def markMiss(self,x,y, color = 'red'):
        self.t.up()
        scaledX = (self.scalar/2)+ (self.scalar*(x-1))
        scaledY = (self.scalar/2)+ (self.scalar*(y-1))
        self.t.setposition(scaledX,scaledY)
        self.t.dot(self.scalar*(2/3),color)

    

    def generateShips(self):
        for ship in range(self.numShips):            
            x = random.randrange(1,self.size+1)
            y = random.randrange(1,self.size+1)
            self.shipLocations.append((x,y))
            if y + 2 > self.size:
                xORy = 1
            elif x +2 > self.size:
                xORy = 0
            else:
                xORy = random.randrange(0,2)
                
            if xORy == 0:
                self.shipLocations.append((x,y+1))
                self.shipLocations.append((x,y+2))                
            else:
                self.shipLocations.append((x+1,y))
                self.shipLocations.append((x+2,y))
                
            
    def showShips(self):
        def fillSquare(t,x,y,color='black'):
            t.up()
            scaledX = self.scalar*(x-1)
            scaledY = self.scalar*(y-1)
            t.setposition(scaledX,scaledY)
            t.fillcolor(color)
            t.fill(True)
            for i in range(4):
                t.forward(self.scalar)
                t.left(90)
            t.fill(False)
        for x,y in self.shipLocations:
            fillSquare(self.t,x,y)
        
        
    def guess(self,x,y):
        if (x,y) in self.shipLocations:
            self.markHit(x,y)
            return True
        else:
            self.markMiss(x,y)
            return False
        
    def getShipLocations(self):
        return self.shipLocations

    def getSize(self):
        return self.size

    def getScalar(self):
        return self.scalar

    def getNumShips(self):
        return self.numShips

##def main():
##    g = Grid()
##    g.setScreen()
##    g.drawGrid()
##    g.generateShips()
##    g.showShips()
##    g.guess(5,5)
##    g.guess(2,7)
##    g.guess(7,2)
##    
##    
##
##main()
    
        

        
                


    
            
