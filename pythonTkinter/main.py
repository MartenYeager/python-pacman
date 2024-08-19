import ghost as gh
import player as pl
import numpy
import tkinter as tk


class gridUnit:
    #a grid unit is 50 X 50 (500 / 10)
    content = None
    canvasID = None
    #gridX = None
    #gridY = None
    center = None
    
    def __init__(self, content, size, gridX, gridY):
        self.content = content  # EMPTY, PALLET, WALL
        #self.gridX = int(gridX)
        #self.gridY = int(gridY)
        self.center = (gridX * size + size / 2, gridY * size + size / 2)

    def setContent(self, canvas, content):  #Used to update grids with eaten pallets
        self.content = content
        canvas.delete(self.canvasID)

    def setCanvasID(self, ID):
        self.canvasID = ID;


def meetsWallCondition(x, y):
    wallCondition = (
        (x == 2 and (y >= 6 and y <= 8)) or
        (x == 2 and (y >= 2 and y <= 4)) or
        (x == 8 and (y >= 6 and y <= 8)) or
        (x == 8 and (y >= 2 and y <= 4)) or

        (y == 8 and (x >= 4 and x <= 6)) or

        #Home base
        (x == 4 and (y >= 4 and y <= 6)) or
        (x == 6 and (y >= 4 and y <= 6)) or
        (x == 5 and y == 6)
    )
    return wallCondition


def meetsEmptyCondition(x, y):
    emptyCondition = (
        (x == 5 and y == 5) or
        (x == 5 and y == 4) or
        (x == 1 and y == 5)
    )
    return emptyCondition

def meetsSuperCondition(x, y):
    superCondition = (
        (x == 1 and y == 1) or
        (x == 1 and y == 9) or
        (x == 9 and y == 1) or
        (x == 9 and y == 9)
    )
    return superCondition

def innitGrid(gridSize, unitSize):
    grid = numpy.ndarray(shape=(gridSize[0], gridSize[1]), dtype=gridUnit)

    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            # print(gridX, ' : ', gridY)

            if (gridX == 0 or gridX == len(grid) - 1 or gridY == 0 or gridY == len(grid) - 1) or meetsWallCondition(gridX, gridY):
                content = 'WALL'
            elif meetsEmptyCondition(gridX, gridY):
                content = 'EMPTY'
            elif meetsSuperCondition(gridX, gridY):
                content = 'SUPER'
            else:
                content = 'PALLET'

            grid[gridX][gridY] = gridUnit(content, unitSize, gridX, gridY)

    return grid


def drawGrid(grid, canvas):
    sizeModifier = 15
    unitSize = 50

    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            unit = grid[gridX][gridY]
            if unit.content == 'WALL':
                id = canvas.create_rectangle(unit.center[0] - unitSize / 2,
                                             unit.center[1] - unitSize / 2,
                                             unit.center[0] + unitSize / 2,
                                             unit.center[1] + unitSize / 2, fill='blue')
            elif unit.content == 'PALLET':
                id = canvas.create_oval(unit.center[0] - unitSize / 2 + sizeModifier,
                                        unit.center[1] - unitSize / 2 + sizeModifier,
                                        unit.center[0] + unitSize / 2 - sizeModifier,
                                        unit.center[1] + unitSize / 2 - sizeModifier, fill='beige')
            elif unit.content == 'SUPER':
                id = canvas.create_oval(unit.center[0] - unitSize / 2,
                                        unit.center[1] - unitSize / 2,
                                        unit.center[0] + unitSize / 2,
                                        unit.center[1] + unitSize / 2, fill='beige')
            unit.setCanvasID(id)


def innitWindow():
    root = tk.Tk()
    screenWidth = 550
    screenHeight = 550
    screenDimensions = str(screenWidth) + 'x' + str(screenHeight)
    root.geometry(screenDimensions)

    playerSizeModifier = 10

    unitSize = 50
    gridSize = (int(screenWidth / unitSize), int(screenHeight / unitSize))

    grid = innitGrid(gridSize, unitSize)

    canvasBackground = tk.Canvas(root, width=550, height=550, background='black')
    drawGrid(grid, canvasBackground)

    spawn = grid[1][5].center
    spawn1 = grid[9][1].center
    spawn2 = grid[9][9].center
    spawn3 = grid[7][5].center
    offset = unitSize / 2

    #temp = canvasBackground.create_oval(spawn[0] - offset + sizeModifier, spawn[1] - offset + sizeModifier, spawn[0] + offset - sizeModifier, spawn[1] + offset - sizeModifier, fill='gold')
    playerID = canvasBackground.create_oval(spawn[0] - offset + playerSizeModifier,
                                            spawn[1] - offset + playerSizeModifier,
                                            spawn[0] + offset - playerSizeModifier,
                                            spawn[1] + offset - playerSizeModifier, fill='gold')
    player = pl.Player(root, canvasBackground, playerID, spawn[0], spawn[1])
    #temp1 = canvasBackground.create_oval(spawn1[0] - offset + sizeModifier, spawn1[1] - offset + sizeModifier, spawn1[0] + offset - sizeModifier, spawn1[1] + offset - sizeModifier, fill='red')
    ghost1 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn1[0] - offset + 0,
                                                                        spawn1[1] - offset + 0,
                                                                        spawn1[0] + offset - 0,
                                                                        spawn1[1] + offset - 0,
                                                                        fill='red'), 1, -5, 0, spawn1[0], spawn1[1])
    #print(str(ghost1.canvasID) + ' = ' + str(ghost1.x) + " : " + str(ghost1.y))
    #temp2 = canvasBackground.create_oval(spawn2[0] - offset + sizeModifier, spawn2[1] - offset + sizeModifier, spawn2[0] + offset - sizeModifier, spawn2[1] + offset - sizeModifier, fill='red')
    ghost2 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn2[0] - offset + 0,
                                                                        spawn2[1] - offset + 0,
                                                                        spawn2[0] + offset - 0,
                                                                        spawn2[1] + offset - 0,
                                                                        fill='red'), 2, -5, 0, spawn2[0], spawn2[1])
    #print(str(ghost2.canvasID) + ' = ' + str(ghost2.x) + " : " + str(ghost2.y))
    #temp3 = canvasBackground.create_oval(spawn3[0] - offset + sizeModifier, spawn3[1] - offset + sizeModifier, spawn3[0] + offset - sizeModifier, spawn3[1] + offset - sizeModifier, fill='red')
    ghost3 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn3[0] - offset + 0,
                                                                           spawn3[1] - offset + 0,
                                                                           spawn3[0] + offset - 0,
                                                                           spawn3[1] + offset - 0,
                                                                           fill='red'), 3, 0, -5, spawn3[0], spawn3[1])
    canvasBackground.pack()

    ghost1.animate()
    ghost1.intersectPlayer(player)

    ghost2.animate()
    ghost2.intersectPlayer(player)

    ghost3.animate()
    ghost3.intersectPlayer(player)

    player.animate()
    player.tick()
    player.intersect(grid, unitSize)

    root.mainloop()

def main():
    innitWindow()

main()

