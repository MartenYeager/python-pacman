import numpy

def meetsWallCondition(x, y):
    wallCondition = (
        (x == 2 and (y >= 6 and y <= 8)) or
        (x == 2 and (y >= 2 and y <= 4)) or
        (x == 8 and (y >= 6 and y <= 8)) or
        (x == 8 and (y >= 2 and y <= 4)) or

        (y == 8 and (x >= 4 and x <= 6)) or
        (y == 2 and (x >= 4 and x <= 6)) or

        # Home base
        (x == 4 and (y >= 4 and y <= 6)) or
        (x == 6 and (y >= 4 and y <= 6)) or
        (x == 5 and y == 6) or
        (x == 5 and y == 4)
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
    grid = numpy.ndarray(shape=(gridSize[0], gridSize[1]), dtype=GridUnit)

    for gridX in range(len(grid)):
        for gridY in range(len(grid)):
            if (gridX == 0 or gridX == len(grid) - 1 or
                gridY == 0 or gridY == len(grid) - 1) or meetsWallCondition(gridX, gridY):
                content = 'WALL'
            elif meetsEmptyCondition(gridX, gridY):
                content = 'EMPTY'
            elif meetsSuperCondition(gridX, gridY):
                content = 'SUPER'
            else:
                content = 'PALLET'

            grid[gridX][gridY] = GridUnit(content, unitSize, gridX, gridY)

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


class GridUnit:
    content = None
    canvasID = None
    center = None

    def __init__(self, content, size, gridX, gridY):
        self.content = content  # EMPTY, PALLET, SUPER, WALL
        self.center = (gridX * size + size / 2, gridY * size + size / 2)

    def setContent(self, canvas, content):
        self.content = content
        canvas.delete(self.canvasID)

    def setCanvasID(self, ID):
        self.canvasID = ID
