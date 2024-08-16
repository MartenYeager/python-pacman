class Player:
    canvasID = None
    palletsCollected = 0
    points = 0
    super = False

    x = 0
    y = 0
    radius = 15

    def __init__(self, id, x, y):
        self.canvasID = id

        self.x = x
        self.y = y

    def animate(self, root, canvas):

        root.bind("<KeyPress-Left>", lambda _: canvas.move(self.canvasID, -5, 0))
        root.bind("<KeyPress-Right>", lambda _: canvas.move(self.canvasID, 5, 0))
        root.bind("<KeyPress-Up>", lambda _: canvas.move(self.canvasID, 0, -5))
        root.bind("<KeyPress-Down>", lambda _: canvas.move(self.canvasID, 0, 5))

    def kill(self):
        print("Player has been killed")
        exit(0)
        pass

    def intersect(self):
        pass
