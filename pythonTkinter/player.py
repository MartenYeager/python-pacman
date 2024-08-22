import math
import screens as sc
import tkinter as tk


class Player:
    canvasID = None
    canvas = None
    root = None
    killSwitch = False

    lives = 3
    labelLives = None
    palletsCollected = 0
    labelPallets = None
    ghostEaten = 0
    labelGhost = None
    super = False
    labelSuper = None

    x = 0
    spawnX = 0
    y = 0
    spawnY = 0
    radius = 15

    speedX = 0
    speedY = 0

    def __init__(self, root, canvas, id, x, y):
        self.canvas = canvas
        self.canvasID = id
        self.root = root

        self.labelLives = tk.StringVar()
        self.labelPallets = tk.StringVar()
        self.labelGhost = tk.StringVar()
        self.labelSuper = tk.StringVar()

        self.x = x
        self.spawnX = x
        self.y = y
        self.spawnY = y

    def toggleSuper(self):
        self.super = not self.super

    def move(self, speedX, speedY):
        self.speedX = speedX
        self.speedY = speedY

        if not self.killSwitch:
            self.canvas.move(self.canvasID, speedX, speedY)

    # Will cause an error if the screen gets changed
    def tick(self):
        x1, y1, x2, y2 = self.canvas.coords(self.canvasID)

        self.x = (x1 + x2) / 2
        self.y = (y1 + y2) / 2

        self.labelLives.set('Lives: ' + str(self.lives))
        self.labelPallets.set('Pallets: ' + str(self.palletsCollected))
        self.labelGhost.set('Ghosts: ' + str(self.ghostEaten))
        self.labelSuper.set('Super: ' + str(self.super))

        if not self.killSwitch:
            self.root.after(20, lambda: self.tick())

    def animate(self):
        self.root.bind("<KeyPress-Left>", lambda _: self.move(-5, 0))
        self.root.bind("<KeyPress-Right>", lambda _: self.move(5, 0))
        self.root.bind("<KeyPress-Up>", lambda _: self.move(0, -5))
        self.root.bind("<KeyPress-Down>", lambda _: self.move(0, 5))

    def kill(self):
        if self.lives <= 1:
            self.killSwitch = True

            sc.innitEndScreen(self.root, self.labelPallets, self.labelGhost)
        else:
            # Can cause spawn camping
            self.lives -= 1
            self.canvas.coords(self.canvasID,
                               self.spawnX - self.radius,
                               self.spawnY - self.radius,
                               self.spawnX + self.radius,
                               self.spawnY + self.radius)

    def intersect(self, grid, unitSize):
        gridX = int(self.x / unitSize)
        gridY = int(self.y / unitSize)

        for x in range(-1, 2):
            for y in range(-1, 2):
                # Can cause index out of range error if player clips through outer walls
                unit = grid[gridX + x][gridY + y]
                unitX = unit.center[0]
                unitY = unit.center[1]

                if unit.content == 'PALLET':
                    dx = abs(unitX - self.x)
                    dy = abs(unitY - self.y)

                    d = math.sqrt(dx**2 + dy**2)

                    if d <= (self.radius + 10):
                        self.palletsCollected += 1
                        unit.setContent(self.canvas, 'EMPTY')

                elif unit.content == 'WALL':
                    Xn = max(unitX - 25, min(self.x, unitX + 25))
                    Yn = max(unitY - 25, min(self.y, unitY + 25))

                    # Calculate the distance between the nearest point and the center of the circle
                    Dx = Xn - self.x
                    Dy = Yn - self.y

                    # Return True if the distance is less than or equal to the radius squared
                    if (Dx * Dx + Dy * Dy) <= self.radius**2:
                        self.canvas.move(self.canvasID, -self.speedX * 2, -self.speedY * 2)

                elif unit.content == 'SUPER':
                    dx = abs(unitX - self.x)
                    dy = abs(unitY - self.y)

                    d = math.sqrt(dx ** 2 + dy ** 2)

                    if d <= (self.radius + 25):
                        if not self.super:
                            self.palletsCollected += 1
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