import math


class Player:
    canvasID = None
    canvas = None
    root = None
    palletsCollected = 0
    points = 0
    super = False

    speedX = 0
    speedY = 0

    x = 0
    y = 0
    radius = 15

    def __init__(self, root, canvas, id, x, y):
        self.canvas = canvas
        self.canvasID = id
        self.root = root

        self.x = x
        self.y = y

    def toggleSuper(self):
        self.super = not self.super

    def move(self, speedX, speedY):
        self.speedX = speedX
        self.speedY = speedY

        self.canvas.move(self.canvasID, speedX, speedY)

    def tick(self):
        x1, y1, x2, y2 = self.canvas.coords(self.canvasID)

        #self.lastX = self.x
        #self.lastY = self.y

        self.x = (x1 + x2) / 2
        self.y = (y1 + y2) / 2

        #self.speedX = self.lastX - self.x
        #self.speedY = self.lastY - self.y

        self.root.after(20, lambda: self.tick())

    def animate(self):
        self.root.bind("<KeyPress-Left>", lambda _: self.move(-5, 0))
        self.root.bind("<KeyPress-Right>", lambda _: self.move(5, 0))
        self.root.bind("<KeyPress-Up>", lambda _: self.move(0, -5))
        self.root.bind("<KeyPress-Down>", lambda _: self.move(0, 5))

    def kill(self):
        print("Player has been killed")
        print("Pallets collected: " + str(self.palletsCollected))
        #print("Ghosts eaten: " + self.points)
        exit(0)

    def intersect(self, grid, unitSize):
        gridX = int(self.x / unitSize)
        gridY = int(self.y / unitSize)

        for x in range(-1, 2):
            for y in range(-1, 2):
                # Can cause index out of range error if player clips through outer walls
                unit = grid[gridX + x][gridY + y]

                if unit.content == 'PALLET':
                    unitX = unit.center[0]
                    unitY = unit.center[1]

                    dx = abs(unitX - self.x)
                    dy = abs(unitY - self.y)

                    d = math.sqrt(dx**2 + dy**2)

                    if d <= (self.radius + 10):
                        #print('Intersect pallet')
                        self.palletsCollected += 1
                        unit.setContent(self.canvas, 'EMPTY')
                elif unit.content == 'WALL':
                    # Sadly, this cheese doesn't work with the corners
                    unitX = unit.center[0]
                    unitY = unit.center[1]

                    dx = abs(unitX - self.x)
                    dy = abs(unitY - self.y)

                    d = math.sqrt(dx ** 2 + dy ** 2)

                    if d < (self.radius + 25):
                        #print(str(self.speedX) + " : " + str(self.speedY))
                        self.canvas.move(self.canvasID, -self.speedX * 2, -self.speedY * 2)
                        #print('Intersect wall')
                elif unit.content == 'SUPER':
                    unitX = unit.center[0]
                    unitY = unit.center[1]

                    dx = abs(unitX - self.x)
                    dy = abs(unitY - self.y)

                    d = math.sqrt(dx ** 2 + dy ** 2)

                    if d <= (self.radius + 25):
                        #pass
                        self.toggleSuper()
                        if unit.content != 'EMPTY':
                            unit.setContent(self.canvas, 'EMPTY')
                        self.root.after(6000, lambda: self.toggleSuper())
                elif unit.content == 'EMPTY':
                    pass
                else:
                    print('Invalid Content')
                    exit(-1)

        self.root.after(40, lambda: self.intersect(grid, unitSize))