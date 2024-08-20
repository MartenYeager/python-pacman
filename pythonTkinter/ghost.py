import math


def route1(ghost):
    x = ghost.x
    y = ghost.y
    # print(str(x) + ' : ' + str(y))
    if x == 75 and y == 75:
        ghost.speedX = 0
        ghost.speedY = 5

    elif x == 75 and y == 475:
        ghost.speedX = 5
        ghost.speedY = 0

    elif x == 475 and y == 475:
        ghost.speedX = 0
        ghost.speedY = -5

    elif x == 475 and y == 75:
        ghost.speedX = -5
        ghost.speedY = 0


def route2(ghost):
    x = ghost.x
    y = ghost.y
    # print(str(x) + ' : ' + str(y))
    if x == 75 and y == 475:
        ghost.speedX = 0
        ghost.speedY = -5

    elif x == 75 and y == 75:
        ghost.speedX = 5
        ghost.speedY = 0

    elif x == 475 and y == 75:
        ghost.speedX = 0
        ghost.speedY = 5

    elif x == 475 and y == 475:
        ghost.speedX = -5
        ghost.speedY = 0


def route3(ghost):
    x = ghost.x
    y = ghost.y
    #print(str(x) + ' : ' + str(y))
    if x == 375 and y == 175:
        ghost.speedX = -5
        ghost.speedY = 0

    elif x == 175 and y == 175:
        ghost.speedX = 0
        ghost.speedY = 5

    elif x == 175 and y == 375:
        ghost.speedX = 5
        ghost.speedY = 0

    elif x == 375 and y == 375:
        ghost.speedX = 0
        ghost.speedY = -5


def route4(ghost):
    x = ghost.x
    y = ghost.y
    # print(str(x) + ' : ' + str(y))
    if x == 375 and y == 375:
        ghost.speedX = -5
        ghost.speedY = 0

    elif x == 175 and y == 375:
        ghost.speedX = 0
        ghost.speedY = -5

    elif x == 175 and y == 175:
        ghost.speedX = 5
        ghost.speedY = 0

    elif x == 375 and y == 175:
        ghost.speedX = 0
        ghost.speedY = 5


class Ghost:
    canvasID = None
    canvas = None
    root = None

    route = None
    killed = False

    initSpeedX = 0
    speedX = 0
    initSpeedY = 0
    speedY = 0

    spawnX = 0
    spawnY = 0
    x = 0
    y = 0
    radius = 25

    def __init__(self, root, canvas, id, route, initSpeedX, initSpeedY, x, y):
        self. canvas = canvas
        self.canvasID = id
        self.root = root
        self.route = route

        self.initSpeedX = initSpeedX
        self.speedX = initSpeedX
        self.initSpeedY = initSpeedY
        self.speedY = initSpeedY

        self.spawnX = x
        self.spawnY = y
        self.x = x
        self.y = y

    def animate(self):
        xTL, yTL, xBR, yBR = self.canvas.coords(self.canvasID)
        self.x = (xTL + xBR) / 2
        self.y = (yTL + yBR) / 2

        if not self.killed:
            # Route
            if self.route == 1:
                route1(self)
            elif self.route == 2:
                route2(self)
            elif self.route == 3:
                route3(self)
            elif self.route == 4:
                route4(self)
            else:
                print('Invalid route')
                exit(-1)

        if not self.killed:
            self.canvas.move(self.canvasID, self.speedX, self.speedY)

        self.root.after(40, lambda: self.animate())

    def kill(self):
        if not self.killed:
            print('Ghost ' + str(self.canvasID) + ' has been killed')
            self.killed = True
            self.canvas.coords(self.canvasID, 250, 250, 300, 300)
            self.speedX = self.initSpeedX
            self.speedY = self.initSpeedY
            self.root.after(4000, lambda: self.kill())
        else:
            print('Ghost ' + str(self.canvasID) + ' is alive')
            self.killed = False
            self.canvas.coords(self.canvasID, self.spawnX - 25, self.spawnY - 25, self.spawnX + 25, self.spawnY + 25)

    def intersectPlayer(self, player):
        dx = abs(self.x - player.x)
        dy = abs(self.y - player.y)

        d = math.sqrt(dx**2 + dy**2)

        if d <= (self.radius + player.radius):
            if player.super:
                self.kill()
            else:
                player.kill()
        self.root.after(40, lambda: self.intersectPlayer(player))
