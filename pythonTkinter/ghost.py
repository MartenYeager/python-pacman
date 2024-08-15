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
    x = None
    y = None
    #speedInnit = 5
    speedX = -5
    speedY = 0
    def __init__(self, id, route, x, y):
        self.canvasID = id
        self.route = route
        self.x = x
        self.y = y


    def animate(self, root, canvas):
        canvas.move(self.canvasID, self.speedX, self.speedY)
        xTL, yTL, xBR, yBR = canvas.coords(self.canvasID)

        self.x = (xTL + xBR) / 2
        self.y = (yTL + yBR) / 2

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

        #canvas.move(self.canvasID, self.speedX, self.speedY)

        root.after(40, lambda: self.animate(root, canvas))

