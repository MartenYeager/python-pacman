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


def route3a():
    pass


class Ghost:
    canvasID = None
    route = None
    killed = False
    #speedInnit = 5
    speedX = -5
    speedY = 0

    x = 0
    y = 0
    radius = 25

    def __init__(self, id, route, x, y):
        self.canvasID = id
        self.route = route

        self.x = x
        self.y = y

        #self.intersectPlayer()

    def animate(self, root, canvas):
        canvas.move(self.canvasID, self.speedX, self.speedY)
        xTL, yTL, xBR, yBR = canvas.coords(self.canvasID)

        # Route
        if self.route == 1:
            route1(self, xTL, yTL, xBR, yBR)
        elif self.route == 2:
            route2(self, xTL, yTL, xBR, yBR)
        elif self.route == 3:
            pass
        else:
            print('Invalid route')
            exit(-1)

        self.x = (xTL + xBR) / 2
        self.y = (yTL + yBR) / 2

        root.after(40, lambda: self.animate(root, canvas))


    def kill(self):
        pass
    def intersectPlayer(self, root, player):
        dx = abs(self.x - player.x)
        dy = abs(self.y - player.y)

        d = math.sqrt(dx**2 + dy**2)

        if d <= (self.radius + player.radius):
            player.kill()
        else:
            root.after(40, lambda: self.intersectPlayer(root, player))
