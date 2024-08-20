import grid as gr
import ghost as gh
import player as pl
import tkinter as tk


def innitWindow():
    root = tk.Tk()
    screenWidth = 550
    screenHeight = 550
    screenDimensions = str(screenWidth) + 'x' + str(screenHeight)
    root.geometry(screenDimensions)

    playerSizeModifier = 10

    unitSize = 50
    gridSize = (int(screenWidth / unitSize), int(screenHeight / unitSize))

    grid = gr.innitGrid(gridSize, unitSize)

    canvasBackground = tk.Canvas(root, width=550, height=550, background='black')
    gr.drawGrid(grid, canvasBackground)

    spawn = grid[1][5].center
    spawn1 = grid[9][1].center
    spawn2 = grid[9][9].center
    spawn3 = grid[7][5].center
    offset = unitSize / 2

    playerID = canvasBackground.create_oval(spawn[0] - offset + playerSizeModifier,
                                            spawn[1] - offset + playerSizeModifier,
                                            spawn[0] + offset - playerSizeModifier,
                                            spawn[1] + offset - playerSizeModifier, fill='gold')
    player = pl.Player(root, canvasBackground, playerID, spawn[0], spawn[1])

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

    canvasBackground.pack()

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

    root.mainloop()


def main():
    innitWindow()


if "__main__":
    main()
