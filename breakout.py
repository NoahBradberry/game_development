import tkinter as tk

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PLAYER_WIDTH = 160
PLAYER_HEIGHT = 15
BRICK_WIDTH = 80
BRICK_HEIGHT = 30



root = tk.Tk()
root.title("Breakout")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()


def start():
    global player 
    player = canvas.create_rectangle(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, SCREEN_WIDTH // 2 + PLAYER_WIDTH// 2, SCREEN_HEIGHT, fill = "white")
    

#Brick Formation
columns = 12
rows = 6

bricks = []

def create_brick_formation():
    bricks.clear()
    start_x = 20
    start_y = 40
    #colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    colors = ["red4", "red", "orange", "yellow", "green", "cyan"]

    for r in range(rows):
        for c in range(columns):
            x = start_x + c * BRICK_WIDTH
            y = start_y + r * BRICK_HEIGHT + 1

            brick = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, fill = colors[r])
            
            bricks.append(brick)

#Player Movement
def move_left(event):
    if canvas.coords(player)[0] > 0:
        canvas.move(player, -15, 0)
def move_right(event):
    if canvas.coords(player)[2] < SCREEN_WIDTH:
        canvas.move(player, 20, 0)


root.bind("<KeyPress-Left>", move_left)
root.bind("<Right>", move_right)


alive = True

def game_loop():
    global alive
    root.after(40, game_loop)

def reset():
    create_brick_formation()
    start()



reset()
root.mainloop()