import tkinter as tk
import random
import math
import threading
import time


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PLAYER_LENGTH = 25
PLAYER_VELO = 5
ENEMY_LENGTH = 25
ENEMY_VELO = 4

root = tk.Tk()
root.title("Top-Down Shooter")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()

def reset(event = None):
    global player, enemies
    enemies = []
    canvas.delete("all")
    player = canvas.create_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2 + PLAYER_LENGTH, SCREEN_HEIGHT // 2 + PLAYER_LENGTH, fill = "white")

def make_enemy():
    global enemy
    spawn_side = random.randint(1, 4)
    start_x = random.randint(0, SCREEN_WIDTH)
    start_y = random.randint(0, SCREEN_HEIGHT)


    if spawn_side == 1:
        enemy = canvas.create_rectangle(- ENEMY_LENGTH, start_y , 0, start_y + ENEMY_LENGTH, fill = "red" )
        enemies.append(enemy)
    elif spawn_side == 2:
        enemy = canvas.create_rectangle(start_x, SCREEN_HEIGHT , start_x + ENEMY_LENGTH, SCREEN_HEIGHT + ENEMY_LENGTH, fill = "red" )
        enemies.append(enemy)
    elif spawn_side == 3:
        enemy = canvas.create_rectangle(SCREEN_WIDTH, start_y, SCREEN_WIDTH + ENEMY_LENGTH, start_y + ENEMY_LENGTH, fill = "red")
        enemies.append(enemy)
    elif spawn_side == 4:
         enemy = canvas.create_rectangle(start_x, 0 , start_x + ENEMY_LENGTH, 0 - ENEMY_LENGTH, fill = "red")
         enemies.append(enemy)
    
    

    root.after(2000, make_enemy)



    


def move_enemies():
    px1, py1, px2, py2 = canvas.coords(player)
    player_center_x = (px2 + px1) / 2
    player_center_y = (py2 + py1) / 2

    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.coords(enemy)
        enemy_center_x = (ex2 + ex1) / 2
        enemy_center_y = (ey2 + ey1) / 2

        dx = player_center_x - enemy_center_x
        dy = player_center_y - enemy_center_y

        distance = math.sqrt(dx**2 + dy**2)

        if distance == 0:
            continue  
        


        move_x = (dx / distance) * ENEMY_VELO
        move_y = (dy / distance) * ENEMY_VELO

        canvas.move(enemy, move_x, move_y)


          

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
root.bind("r", reset)

def game_loop():

    global enemy
    
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
    
    
    move_enemies()
    root.after(16, game_loop)



reset()
game_loop()
make_enemy()
root.mainloop()