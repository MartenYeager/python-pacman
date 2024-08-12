import keyboard
import numpy
import tkinter as tk

class gridUnit:
    #a grid unit is 50 X 50 (500 / 10)
    content = None
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

def innitWindow():
    root = tk.Tk()
    root.geometry('500x500')

    canvas = tk.Canvas(root, width=500, height=500, background='black')
    #drawing code
    canvas.pack()

    root.mainloop()

def main():
    #innitWindow()

    gridSize = 10
    grid = numpy.ndarray(shape=(gridSize, gridSize), dtype=gridUnit)

    for gridY in range(10):
        for gridX in range(10):
            #print(gridX, ' : ', gridY)

            if (gridX == 0 or gridX == 9 or gridY == 0 or gridY == 9):
                #print('WALL')
                content = 'WALL'
            else:
                content = 'EMTPY'
            grid[gridX][gridY] = gridUnit(content, 50, gridX, gridY)

    for gridY in range(10):
        for gridX in range(10):
            print(grid[gridX][gridY].content)


main()
