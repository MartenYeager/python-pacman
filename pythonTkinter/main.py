import ghost
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

    def setContent(self, content):  #Used to update grids with eaten pallets
        self.content = content

    def setCanvasID(self, ID):
        self.canvasID = ID;


class Player:
    canvasID = None

    def __init__(self, id):
        self.canvasID = id

    def intersectPallet(self, canvas, id):
        pass


def animetion(root, canvas, id, speed):
    #speed = 5
    #dy = 0

    canvas.move(id, speed, 0)
    xTL, yTL, xBR, yBR = canvas.coords(id)
    #print(id, ': 1 = ', xTL, ' : ', yTL)
    #print(id, ': 2 = ', xBR, ' : ', yBR)

    if xBR >= 500 or xTL <= 50:
        speed
        speed = -speed  # Reverse the horizontal direction

    # Schedule the next move
    root.after(40, lambda: animetion(root, canvas, id, speed))


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


def innitGrid(gridSize, unitSize):
    grid = numpy.ndarray(shape=(gridSize[0], gridSize[1]), dtype=gridUnit)

    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            # print(gridX, ' : ', gridY)

            if (gridX == 0 or gridX == len(grid) - 1 or gridY == 0 or gridY == len(grid) - 1) or meetsWallCondition(gridX, gridY):
                content = 'WALL'
            elif meetsEmptyCondition(gridX, gridY):
                content = 'EMPTY'
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
                #id = canvas.create_rectangle(gridX * unitSize, gridY * unitSize, (gridX + 1) * unitSize, (gridY + 1) * unitSize, fill='blue')
                id = canvas.create_rectangle(unit.center[0] - unitSize / 2, unit.center[1] - unitSize / 2, unit.center[0] + unitSize / 2, unit.center[1] + unitSize / 2, fill='blue')
            elif unit.content == 'PALLET':
                id = canvas.create_oval(unit.center[0] - unitSize / 2 + sizeModifier, unit.center[1] - unitSize / 2 + sizeModifier, unit.center[0] + unitSize / 2 - sizeModifier, unit.center[1] + unitSize / 2 - sizeModifier, fill='beige')
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

    canvasBackground = tk.Canvas(root, width=550, height=550, background='white')
    drawGrid(grid, canvasBackground)

    spawn = grid[1][5].center
    spawn1 = grid[9][1].center
    spawn2 = grid[9][9].center
    spawn3 = grid[7][5].center
    offset = unitSize / 2

    #temp = canvasBackground.create_oval(spawn[0] - offset + sizeModifier, spawn[1] - offset + sizeModifier, spawn[0] + offset - sizeModifier, spawn[1] + offset - sizeModifier, fill='gold')
    player = Player(canvasBackground.create_oval(spawn[0] - offset + playerSizeModifier, spawn[1] - offset + playerSizeModifier,
                                        spawn[0] + offset - playerSizeModifier, spawn[1] + offset - playerSizeModifier, fill='gold'))
    #temp1 = canvasBackground.create_oval(spawn1[0] - offset + sizeModifier, spawn1[1] - offset + sizeModifier, spawn1[0] + offset - sizeModifier, spawn1[1] + offset - sizeModifier, fill='red')
    ghost1 = ghost.Ghost(canvasBackground.create_oval(spawn1[0] - offset + 0, spawn1[1] - offset + 0,
                                        spawn1[0] + offset - 0, spawn1[1] + offset - 0,
                                        fill='red'), 1, spawn1[0], spawn1[1])
    #temp2 = canvasBackground.create_oval(spawn2[0] - offset + sizeModifier, spawn2[1] - offset + sizeModifier, spawn2[0] + offset - sizeModifier, spawn2[1] + offset - sizeModifier, fill='red')
    ghost2 = ghost.Ghost(canvasBackground.create_oval(spawn2[0] - offset + 0, spawn2[1] - offset + 0,
                                         spawn2[0] + offset - 0, spawn2[1] + offset - 0,
                                         fill='red'), 2, spawn2[0], spawn2[1])
    #temp3 = canvasBackground.create_oval(spawn3[0] - offset + sizeModifier, spawn3[1] - offset + sizeModifier, spawn3[0] + offset - sizeModifier, spawn3[1] + offset - sizeModifier, fill='red')
    temp3 = canvasBackground.create_oval(spawn3[0] - offset + 0, spawn3[1] - offset + 0,
                                         spawn3[0] + offset - 0, spawn3[1] + offset - 0,
                                         fill='red')
    canvasBackground.pack()

    #animetion(root, canvasBackground, ghost1.canvasID, -5)
    ghost1.animate(root, canvasBackground)
    #animetion(root, canvasBackground, ghost2.canvasID, -5)
    ghost2.animate(root, canvasBackground)

    root.bind("<KeyPress-Left>", lambda _: canvasBackground.move(player.canvasID, -5, 0))
    root.bind("<KeyPress-Right>", lambda _: canvasBackground.move(player.canvasID, 5, 0))
    root.bind("<KeyPress-Up>", lambda _: canvasBackground.move(player.canvasID, 0, -5))
    root.bind("<KeyPress-Down>", lambda _: canvasBackground.move(player.canvasID, 0, 5))

    root.mainloop()

def main():
    innitWindow()

main()

