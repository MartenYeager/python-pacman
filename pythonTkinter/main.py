import screens as sc
import tkinter as tk

def main():
    root = tk.Tk()
    screenWidth = 650
    screenHeight = 550
    screenDimensions = str(screenWidth) + 'x' + str(screenHeight)
    root.geometry(screenDimensions)

    sc.innitMainScreen(root)

    root.mainloop()


if "__main__":
    main()
