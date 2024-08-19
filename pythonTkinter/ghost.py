import math


def route1(ghost, xTL, yTL, xBR, yBR):
    if xTL <= 50 and yTL == 50:
        ghost.speedX = 0
        ghost.speedY = 5

    elif yBR >= 500 and xBR == 100:
        ghost.speedX = 5
        ghost.speedY = 0

    elif xBR >= 500 and yBR == 500:
        ghost.speedX = 0
        ghost.speedY = -5

    elif yTL <= 50 and xTL == 450:
        ghost.speedX = -5
        ghost.speedY = 0


def route2(ghost, xTL, yTL, xBR, yBR):
    if xTL <= 50 and yBR == 500:
        ghost.speedX = 0
        ghost.speedY = -5

    elif xBR == 100 and yBR  <= 100:
        ghost.speedX = 5
        ghost.speedY = 0

    elif xBR >= 500 and yBR == 100:
        ghost.speedX = 0
        ghost.speedY = 5

    elif xBR <= 500 and yBR == 500:
        ghost.speedX = -5
        ghost.speedY = 0


def route3(ghost, xTL, yTL, xBR, yBR):
    x = ghost.x
    y = ghost.y
    #print(str(x) + ' : ' + str(y))
    if x == 375 and y == 175:
        ghost.speedX = -5
        ghost.speedY = 0
        #print('Ping1')
        #print(str(ghost.x) + ' : ' + str(ghost.y))

    elif x == 180 and y == 170:
        ghost.speedX = 0
        ghost.speedY = 5
        #print('Ping2')
        #print(str(ghost.x) + ' : ' + str(ghost.y))

    elif x == 175 and y == 370:
        ghost.speedX = 5
        ghost.speedY = 0
        #print('Ping3')
        #print(str(ghost.x) + ' : ' + str(ghost.y))

    elif x == 370 and y == 375:
        ghost.speedX = 0
        ghost.speedY = -5
        #print('Ping4')
        #print(str(ghost.x) + ' : ' + str(ghost.y))


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

        #self.intersectPlayer()

    def animate(self):
        if not self.killed:
            self.canvas.move(self.canvasID, self.speedX, self.speedY)

        xTL, yTL, xBR, yBR = self.canvas.coords(self.canvasID)
        if not self.killed:
            # Route
            if self.route == 1:
                route1(self, xTL, yTL, xBR, yBR)
            elif self.route == 2:
                route2(self, xTL, yTL, xBR, yBR)
            elif self.route == 3:
                route3(self, xTL, yTL, xBR, yBR)
            else:
                print('Invalid route')
                exit(-1)

        self.x = (xTL + xBR) / 2
        self.y = (yTL + yBR) / 2

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
