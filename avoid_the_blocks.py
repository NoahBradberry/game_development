import tkinter as tk
import random

#Declare CONSTANTS

SCREEN_WIDTH = 400
SCREEN_HEIGHT = SCREEN_WIDTH * 0.75
PLAYER_SIZE = 30
ENEMY_SIZE = 20

#Build Window
root = tk.Tk()
root.title("Avoid the Blocks")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()

#Make the Player
player = canvas.create_rectangle(180, 250, 180 + PLAYER_SIZE, 250 + PLAYER_SIZE, fill = "magenta")


#Make a list to hold enemies
enemies = []

#make an alive bool
alive = True

#Movement functions

def move_left(event):
    canvas.move(player, -20, 0)
def move_right(event):
    canvas.move(player, 20, 0)


#Binding Buttons
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)


#Enemies
def spawn_enemy():
    x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
    enemy = canvas.create_rectangle(x, 0, x + ENEMY_SIZE, ENEMY_SIZE, fill = "cyan")
    enemies.append(enemy)

def run_game():
    global alive

    if not alive:
        canvas.create_text(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, text = "GAME OVER", fill = "white")
        return
    
    if random.randint(1, 20) == 1:
        spawn_enemy()
    
    for enemy in enemies:
        canvas.move(enemy, 0, 10)

        if canvas.bbox(enemy) and canvas.bbox(player):
            ex1, ey1, ex2, ey2 = canvas.bbox(enemy)
            px1, py1, px2, py2 = canvas.bbox(player)

            if ex1 < px2 and ex2 > px1 and ey1 < py2 and ey2 > py1:
                alive = False

    root.after(50, run_game)
run_game()
root.mainloop()

