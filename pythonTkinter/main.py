import grid as gr
import ghost as gh
import player as pl
import tkinter as tk


def clearScreen(root):
    # TODO: Clear the root
    obj = root.winfo_children();

    for widget in root.winfo_children():
        widget.destroy()
    pass


def innitMainScreen(root):
    clearScreen(root)

    button = tk.Button(root, text="Game Start", command=lambda: innitGameScreen(root))
    button.pack(anchor='e')


def innitEndScreen(root, labelPallets, labelGhost):
    clearScreen(root)

    labelPallets = tk.Label(root, textvariable=labelPallets)
    labelPallets.pack()
    labelGhost = tk.Label(root, textvariable=labelGhost)
    labelGhost.pack()

    button1 = tk.Button(root, text="Game Restart", command=lambda: innitGameScreen(root))
    button1.pack(anchor='e')

    button2 = tk.Button(root, text="Main Screen", command=lambda: innitMainScreen(root))
    button2.pack(anchor='e')
    #exit(0)


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

    # Adds Player UI Labels
    labelPallets = tk.Label(root, textvariable=player.labelPallets)
    #labelPallets.place(relx=0.8, rely=0)
    labelPallets.pack(anchor='ne')
    labelGhost = tk.Label(root, textvariable=player.labelGhost)
    #labelGhost.place(relx=0.8, rely=0)
    labelGhost.pack(anchor='ne')
    labelSuper = tk.Label(root, textvariable=player.labelSuper)
    #labelSuper.place(relx=0.8, rely=0)
    labelSuper.pack(anchor='ne')

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
    #ghost1.intersectPlayer(player)

    ghost2.animate()
    #ghost2.intersectPlayer(player)

    ghost3.animate()
    ghost3.intersectPlayer(player)

    ghost4.animate()
    ghost4.intersectPlayer(player)

    player.animate()
    player.tick()
    player.intersect(grid, unitSize)

    button1 = tk.Button(root, text="Game Restart", command=lambda: innitGameScreen(root))
    button1.pack(anchor='e')

    button2 = tk.Button(root, text="Main Screen", command=lambda: innitMainScreen(root))
    button2.pack(anchor='e')

    button3 = tk.Button(root, text="Game End", command=lambda: innitEndScreen(root, player.labelPallets, player.labelGhost))
    button3.pack(anchor='e')




def main():
    root = tk.Tk()
    screenWidth = 650
    screenHeight = 550
    screenDimensions = str(screenWidth) + 'x' + str(screenHeight)
    root.geometry(screenDimensions)

    #root.after(5000, lambda: innitGameScreen(root))
    #innitGameScreen(root)
    innitMainScreen(root)

    root.mainloop()


if "__main__":
    main()
