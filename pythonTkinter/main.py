import keyboard
import numpy
import tkinter as tk

class gridUnit:
    #a grid unit is 50 X 50 (500 / 10)
    content = None
    canvasID = None
    gridX = None
    gridY = None
    center = None
    
    def __init__(self, content, size, gridX, gridY):
        self.content = content  # EMPTY, PALLET, WALL
        self.gridX = int(gridX)
        self.gridY = int(gridY)
        self.center = [gridX * size, gridY * size]  #This puts the center in the bottom left corner

    def setContent(self, content):  #Used to update grids with eaten pallets
        self.content = content

    def setCanvasID(self, ID):
        self.canvasID = ID;

def meetsWallCondition(x, y):
    wallCondition = (
        (x == 2 and (y >= 6 and y <= 8)) or
        (x == 2 and (y >= 2 and y <= 4)) or
        (x == 8 and (y >= 6 and y <= 8)) or
        (x == 8 and (y >= 2 and y <= 4)) or
        #((x >= 4 and y <= 6) and y == 8) or
        (y == 8 and (x >= 4 and x <= 6)) or

        #Home base
        (x == 4 and (y >= 4 and y <= 6)) or
        (x == 6 and (y >= 4 and y <= 6)) or
        (x == 5 and y == 6)
    )
    return wallCondition
def innitGrid(gridSize, unitSize):
    grid = numpy.ndarray(shape=(gridSize[0], gridSize[1]), dtype=gridUnit)

    #Creates the WALL's of the maze
    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            # print(gridX, ' : ', gridY)

            if (gridX == 0 or gridX == len(grid) - 1 or gridY == 0 or gridY == len(grid) - 1) or meetsWallCondition(gridX, gridY):
                content = 'WALL'
            #elif gridX % 2 != 0 or gridY % 2 != 0:
                #content = 'PALLET'
            else:
                content = 'PALLET'

            grid[gridX][gridY] = gridUnit(content, unitSize, gridX, gridY)

    return grid

def drawGrid(grid, canvas):
    varB = 15
    unitSize = 50

    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            if grid[gridX][gridY].content == 'WALL':
                id = canvas.create_rectangle(gridX * unitSize, gridY * unitSize, (gridX + 1) * unitSize, (gridY + 1) * unitSize, fill='blue')
            elif grid[gridX][gridY].content == 'PALLET':
                id = canvas.create_oval((gridX * unitSize) + varB, (gridY * unitSize) + varB, ((gridX + 1) * unitSize) - varB, ((gridY + 1) * unitSize) - varB, fill='beige')
            grid[gridX][gridY].setCanvasID(id)

def innitWindow():
    root = tk.Tk()
    root.geometry('550x550')    # To bad this is hard coded

    varA = 10


    gridSize = (11, 11)
    unitSize = 50
    grid = innitGrid(gridSize, unitSize)

    # Creates a new canvas for the player
    #player = movingCanvas(root)  # canvas.create_oval(50 + varA, 250 + varA, 100 - varA, 300 - varA, fill='red')
    #player.pack(fill='both')

    canvasBackground = tk.Canvas(root, width=550, height=550, background='white')
    drawGrid(grid, canvasBackground)
    temp = canvasBackground.create_oval(250 + varA, 250 + varA, 300 - varA, 300 - varA, fill='red')  #Center
    canvasBackground.pack()

    root.bind("<KeyPress-Left>", lambda _: canvasBackground.move(temp, -5, 0))
    root.bind("<KeyPress-Right>", lambda _: canvasBackground.move(temp, 5, 0))
    root.bind("<KeyPress-Up>", lambda _: canvasBackground.move(temp, 0, -5))
    root.bind("<KeyPress-Down>", lambda _: canvasBackground.move(temp, 0, 5))

    root.mainloop()

def main():
    innitWindow()

    '''for gridY in range(10):
        for gridX in range(10):
            print(grid[gridX][gridY].content)'''


main()
