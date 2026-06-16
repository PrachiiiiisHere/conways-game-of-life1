import pygame
import random

pygame.init() #starts all the modules of pygame

#making a canvas
width=900
height=800

cellSize=10

ROWS=height//cellSize
COLS=width//cellSize
screen=pygame.display.set_mode((width,height)) #canvas accepts a tuple btw

pygame.display.set_caption("CONWAY'S GAME OF LIFE")

#creating a random grid
grid=[[random.choice([0,1]) for _ in range(COLS)] for _ in range(ROWS)]
#GRID CREATED!

clock=pygame.time.Clock() #for stopping between each run


#===== COUNTING NEIGHBOURS======
def countNeighbour(grid,row,col):
    count=0
    #rc = change in row and cc = change in column
    for rc in (-1,0,1):
        for cc in (-1,0,1):
            if rc == 0 and cc == 0:
                continue
            neighbourRow= row+rc
            neighbourCol=col + cc


            if 0<=neighbourRow<ROWS and 0<=neighbourCol<COLS:
                count += grid[neighbourRow][neighbourCol] #IT WILL fetch values of neighbours it can be either 0 or 1 we simply add them all


    return count


#==== CREATING NEXT GEN======

''' 
1. Any LIVE cell with fewer than 2 live neighbors dies.
   (Underpopulation)

2. Any LIVE cell with 2 or 3 live neighbors survives.

3. Any LIVE cell with more than 3 live neighbors dies.
   (Overpopulation)

4. Any DEAD cell with exactly 3 live neighbors becomes alive.
   (Birth)'''


#start off with a new grid (world) with no living cell 
def nextGen(grid):
    newGrid=[[0 for _ in range(COLS)] for _ in range(ROWS)]

    #visit every cell
    #count the neighbours of each cell
    #check whether THAT cell is alive
    #KEEP IT alive or kill it based on no of neighbours

    for row in range(ROWS):
        for col in range(COLS):

            neighbour=countNeighbour(grid,row,col)

            #if current cell is alive keep it alive
            if grid[row][col]==1: #alive
                if neighbour in(2,3):
                    newGrid[row][col]=1
            
            #if current cell is DEAD and no. of neigh ==3 birth a new one
            else: #dead
                if neighbour==3:
                    newGrid[row][col]=1
            
        # DEAD ONES THAT ARE TO REMAIN DEAD ARE ALREADY TAKEN CARE OF
    return newGrid

#main
running = True

#check for window close
#clear screen
#draw living cells
#show them to screen
#calculate next gen
#wait a bit
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False #STOP the program

    #clear SCREEN
    screen.fill((0,0,0)) # FILL EXPECTS A TUPLE

    #DRAW LIVING CELLS
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col]==1:
                #cell alive draw a rec 
                #for that we gotta find its location/coordinates
                
                #x coordinate that is across
                x=col*cellSize
                y=row*cellSize

                #now DRAW RECT
                pygame.draw.rect(screen,(255,255,255),(x,y,cellSize,cellSize))


    
    #display everything after drawing
    pygame.display.flip()

    #everytime the grid updates
    grid=nextGen(grid)

    clock.tick(10)

pygame.quit()





    





