from Grid import *
from CPUGrid import *
import random

def main():
    cont = True
    while cont:
        title = '*****{}*****'.format('Welcome to Battleship!')
        print(title)

        
        diff = input('Please select your difficulty (easy,medium,hard,impossible: \n')

        if diff == 'easy':
            g = Grid(5)
            cpu = CPUGrid(5)
        elif diff == 'medium':
            g = Grid(10)
            cpu = CPUGrid(10)
        elif diff == 'hard':
            g = Grid(15)
            cpu = CPUGrid(15)
    

        print('OK! Lets set up the board!')
        print('Please wait')

        #Set up user board
        g.drawGrid()
        g.generateShips()

        #Set up cpu board
        cpu.drawGrid()
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

        again = input('Enter exit or replay: ')
        if again == 'exit':
            g.s.bye()
            cpu.s.bye()
            cont = False
        else:
            continue
            g.s.bye()
            cpu.s.bye()
        

main()
    
    
            

    
    
            

    
    
            
