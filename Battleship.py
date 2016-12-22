from Grid import *
from CPUGrid import *
import cTurtle
import random

def main():
    title = '*****{}*****'.format('Welcome to Battleship!')
    print(title)
    
    diff = input('Please select your difficulty (easy,medium,hard,impossible: \n')

    if diff == 'easy':
        g = Grid(5,20)
        cpu = CPUGrid(5,20)

    elif diff == 'medium':
        g = Grid(10,20)
        cpu = CPUGrid(10,20)
    elif diff == 'hard':
        g = Grid(20,20)
        cpu = CPUGrid(20,20)
    else:
        g = Grid(30,20)
        cpu = CPUGrid(30,20)

    print('OK! Lets set up the board!')
    print('Please wait')

    #Set up user board
    #g.setScreen()
    g.drawGrid()
    g.writeTitle('BATTLESHIP - Your Board')
    g.generateShips()

    #Set up cpu board
    #cpu.setScreen()
    cpu.drawGrid()
    cpu.writeTitle('BATTLESHIP - CPU Board')
    cpu.generateShips()
    cpu.showShips()
    

    numShips = g.getNumShips()
    numPlayerHits = 0
    numCPUHits = 0
    print('\n')
    print('Lets play!')

    
    while(numPlayerHits < numShips*3 and numCPUHits < numShips*3):

        #Player Guesses               
        try:
            s = input('Enter a coordinate guess in the form x,y: ')
            lGuess = s.split(',')
            x = int(lGuess[0])
            y = int(lGuess[1])
        except ValueError:
            print('Please enter a valid pair of coordinates: ')

            print('\n')
            continue

        if x > g.getSize() or y > g.getSize() or y < 1 or x < 1 or len(s)<3:
            print('Please enter a pair of coordinates in the range: ')
            print('\n')
            continue       

        if g.guess(x,y):
            print('You got a hit!')
            print('\n')
            numPlayerHits += 1
            
        else:
            print('Sorry, guess again')
            print('\n')


        #CPU Guesses
        if cpu.guess():
            numCPUHits += 1                


    if numPlayerHits == numShips*3:
        print('You got all the ships! Thanks for playing!')
    else:
        print('You lost! All your ships are sunk!')
           
        

main()
    
    
            