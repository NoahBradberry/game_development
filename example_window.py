import tkinter as tk

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

root = tk.Tk()
root.title("Example")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()

root.mainloop()