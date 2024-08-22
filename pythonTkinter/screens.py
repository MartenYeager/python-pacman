import grid as gr
import ghost as gh
import player as pl
import tkinter as tk


def clearScreen(root):
    for widget in root.winfo_children():
        widget.destroy()


def innitMainScreen(root):
    clearScreen(root)

    buttonGame = tk.Button(root, text="Game Start", command=lambda: innitGameScreen(root))
    buttonGame.place(relx=0.45, rely=0.45)


def innitEndScreen(root, labelPallets, labelGhost):
    clearScreen(root)

    labelPallets = tk.Label(root, textvariable=labelPallets)
    labelPallets.pack()
    labelGhost = tk.Label(root, textvariable=labelGhost)
    labelGhost.pack()

    buttonRestart = tk.Button(root, text="Game Restart", command=lambda: innitGameScreen(root))
    buttonRestart.pack()

    buttonMain = tk.Button(root, text="Main Screen", command=lambda: innitMainScreen(root))
    buttonMain.pack()


def innitGameScreen(root):
    clearScreen(root)

    playerSizeModifier = 10
    unitSize = 50
    gridSize = (int(550 / unitSize), int(550 / unitSize))

    # Creates the grid of the maze
    grid = gr.innitGrid(gridSize, unitSize)

    # Creates the canvas upon which the maze is drawn
    canvasBackground = tk.Canvas(root, width=550, height=550, background='black')

    gr.drawGrid(grid, canvasBackground)
    canvasBackground.place(relx=0, rely=0)

    spawn = grid[1][5].center
    spawn1 = grid[9][1].center
    spawn2 = grid[9][9].center
    spawn3 = grid[7][5].center
    offset = unitSize / 2

    # Creates the player obj
    playerID = canvasBackground.create_oval(spawn[0] - offset + playerSizeModifier,
                                            spawn[1] - offset + playerSizeModifier,
                                            spawn[0] + offset - playerSizeModifier,
                                            spawn[1] + offset - playerSizeModifier, fill='gold')
    player = pl.Player(root, canvasBackground, playerID, spawn[0], spawn[1])

    # Adds UI
    labelLives = tk.Label(root, textvariable=player.labelLives)
    labelLives.pack(anchor='ne')
    labelPallets = tk.Label(root, textvariable=player.labelPallets)
    labelPallets.pack(anchor='ne')
    labelGhost = tk.Label(root, textvariable=player.labelGhost)
    labelGhost.pack(anchor='ne')
    labelSuper = tk.Label(root, textvariable=player.labelSuper)
    labelSuper.pack(anchor='ne')

    buttonRestart = tk.Button(root, text="Game Restart", command=lambda: innitGameScreen(root))
    buttonRestart.pack(anchor='e')

    buttonMain = tk.Button(root, text="Main Screen", command=lambda: innitMainScreen(root))
    buttonMain.pack(anchor='e')

    buttonEnd = tk.Button(root, text="Game End", command=lambda: innitEndScreen(root, player.labelPallets, player.labelGhost))
    buttonEnd.pack(anchor='e')

    # Creates the ghost characters
    ghost1 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn1[0] - offset + 0,
                                                                           spawn1[1] - offset + 0,
                                                                           spawn1[0] + offset - 0,
                                                                           spawn1[1] + offset - 0,
                                                                           fill='red'), 1, -5, 0, spawn1[0], spawn1[1])

    ghost2 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn2[0] - offset + 0,
                                                                           spawn2[1] - offset + 0,
                                                                           spawn2[0] + offset - 0,
                                                                           spawn2[1] + offset - 0,
                                                                           fill='red'), 2, -5, 0, spawn2[0], spawn2[1])

    ghost3 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn3[0] - offset + 0,
                                                                           spawn3[1] - offset + 0,
                                                                           spawn3[0] + offset - 0,
                                                                           spawn3[1] + offset - 0,
                                                                           fill='red'), 3, 0, -5, spawn3[0], spawn3[1])

    ghost4 = gh.Ghost(root, canvasBackground, canvasBackground.create_oval(spawn3[0] - offset + 0,
                                                                           spawn3[1] - offset + 0,
                                                                           spawn3[0] + offset - 0,
                                                                           spawn3[1] + offset - 0,
                                                                           fill='red'), 4, 0, 5, spawn3[0], spawn3[1])

    # Starts the logic of the characters and player
    ghost1.animate()
    ghost1.intersectPlayer(player)

    ghost2.animate()
    ghost2.intersectPlayer(player)

    ghost3.animate()
    ghost3.intersectPlayer(player)

    ghost4.animate()
    ghost4.intersectPlayer(player)

    player.animate()
    player.tick()
    player.intersect(grid, unitSize)

