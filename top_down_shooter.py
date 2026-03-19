import tkinter as tk
import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PLAYER_LENGTH = 25
PLAYER_VELO = 5

root = tk.Tk()
root.title("Top-Down Shooter")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()

def reset():
    global player
    #canvas.delete("all")
    player = canvas.create_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2 + PLAYER_LENGTH, SCREEN_HEIGHT // 2 + PLAYER_LENGTH, fill = "white")

keys = {
        "Left": False,
        "Right": False,
        "Up": False,
        "Down": False
}

def key_press(event):
       if event.keysym in keys:
            keys[event.keysym] = True

def key_release(event):
       if event.keysym in keys:
              keys[event.keysym] = False

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

def game_loop():
    
    dx = 0
    dy = 0

    if keys["Left"]:
        dx -= PLAYER_VELO
    elif keys["Right"]:
        dx += PLAYER_VELO
    elif keys["Up"]:
        dy -= PLAYER_VELO
    elif keys["Down"]:
        dy += PLAYER_VELO
    if keys["Left"] and keys["Down"]:
         dx = - math.sqrt(0.5 * (PLAYER_VELO ** 2))
         dy = math.sqrt(0.5 * (PLAYER_VELO ** 2))
    if keys["Left"] and keys["Up"]:
         dx = - math.sqrt(0.5 * (PLAYER_VELO ** 2))
         dy = - math.sqrt(0.5 * (PLAYER_VELO ** 2))
    if keys["Right"] and keys["Down"]:
         dx = math.sqrt(0.5 * (PLAYER_VELO ** 2))
         dy = math.sqrt(0.5 * (PLAYER_VELO ** 2))
    if keys["Right"] and keys["Up"]:
         dx = math.sqrt(0.5 * (PLAYER_VELO ** 2))
         dy = - math.sqrt(0.5 * (PLAYER_VELO ** 2))

    px1, py1, px2, py2 = canvas.coords(player)

    if 0 <= px1 + dx and px2 + dx <= SCREEN_WIDTH:
         canvas.move(player, dx, 0)

    if 0 <= py1 + dy and py2 + dy <= SCREEN_HEIGHT:
        canvas.move(player, 0, dy)

    root.after(16, game_loop)








reset()
game_loop()
root.mainloop()