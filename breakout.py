import tkinter as tk
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
PLAYER_WIDTH = 160
PLAYER_HEIGHT = 15
BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BALL_DIAMETER = 25
POWERUP_DIAMETER = 20



root = tk.Tk()
root.title("Breakout")

canvas = tk.Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = "black")
canvas.pack()

def reset(event = None):
    canvas.delete("all")
    create_brick_formation()
    global player, ball, ball_x_velo, ball_y_velo, alive, powerups, balls
    player = canvas.create_rectangle(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT, SCREEN_WIDTH // 2 + PLAYER_WIDTH// 2, SCREEN_HEIGHT, fill = "white")
    balls = []
    ball = canvas.create_oval(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH //2 + BALL_DIAMETER, SCREEN_HEIGHT // 2 + BALL_DIAMETER, fill = "white")
    balls.append[ball]
    ball_y_velo = 10
    ball_x_velo = 0
    alive = True
    powerups = []
    game_loop()


    

#Brick Formation
columns = 12
rows = 6

bricks = []

def create_brick_formation():
    bricks.clear()
    start_x = 20
    start_y = 40
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
root.bind("r", reset)

def check_bounce_paddle():
    for ball in balls:
        global ball_y_velo, ball_x_velo
        px1, py1, px2, py2 = canvas.bbox(player)
        bx1, by1, bx2, by2 = canvas. bbox(ball)

        if bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1:
            offset = (px1 + PLAYER_WIDTH // 2) - (bx1 + BALL_DIAMETER)
            ball_x_velo = ball_x_velo - (offset/10)


            ball_y_velo = -ball_y_velo

def check_bounce_brick():
    global ball_y_velo, ball_x_velo, powerup, powerups
    for ball in balls:
        for brick in bricks:
            brx1, bry1, brx2, bry2 = canvas.bbox(brick)
            bx1, by1, bx2, by2 = canvas. bbox(ball)

            if bx1 < brx2 and bx2 > brx1 and by1 < bry2 and by2 > bry1:
                canvas.delete(brick)
                bricks.remove(brick)
                ball_y_velo = -ball_y_velo
                offset = (brx1 + PLAYER_WIDTH // 2) - (bx1 + BALL_DIAMETER)
                ball_x_velo = ball_x_velo - (offset/10)
                if random.randint(1, 1) == 1:
                    powerup = canvas.create_oval(brx1 + BRICK_WIDTH // 2 - POWERUP_DIAMETER // 2, bry2, brx1 + BRICK_WIDTH // 2 + POWERUP_DIAMETER // 2, bry2 + POWERUP_DIAMETER, fill = "green")
                    powerups.append(powerup)

def check_bounce_wall():
    global ball_x_velo, ball_y_velo
    for ball in balls:
        bx1, by1, bx2, by2 = canvas.bbox(ball)

        if bx1  < 0:
            ball_x_velo = - ball_x_velo
        elif bx2 > SCREEN_WIDTH:
            ball_x_velo = - ball_x_velo
        
        if by1 < 0:
            ball_y_velo = -ball_y_velo


def check_loss():
    global alive
    for ball in balls:
        bx1, by1, bx2, by2 = canvas.bbox(ball)
        if by2 > SCREEN_HEIGHT:
            balls.remove(ball)
            canvas.delete(ball)
            if len(balls) == 0:
                alive = False

def check_win():
    global ball_x_velo, ball_y_velo

    if len(bricks) == 0:
        ball_y_velo = 0
        ball_y_velo = 0

        canvas.create_text(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, text = "YOU WIN!", fill = "white", font = 100)
        canvas.create_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, text = "Press r to restart", fill = "white", font = 100)

def activate_powerup():
    for ball in balls:
        ball


def check_powerups():
    for powerup in powerups:
        pox1, poy1, pox2, poy2 = canvas.bbox(powerup)
        plx1, ply1, plx2, ply2 = canvas.bbox(player)

        if pox1 < plx2 and pox2 > plx1 and poy1 < ply2 and poy2 > ply1:
            activate_powerup()
            powerups.remove(powerup)
            canvas.delete(powerup)
        
        if poy2 > SCREEN_HEIGHT:
            powerups.remove(powerup)
            canvas.delete(powerup)




alive = True

def game_loop():
    if not alive:
        canvas.create_text(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, text = "GAME OVER", fill = "white", font = 100)
        canvas.create_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, text = "Press r to restart", fill = "white", font = 100)

    else:
        canvas.move(ball, ball_x_velo, ball_y_velo)
        check_bounce_paddle()
        check_bounce_brick()
        check_bounce_wall()
        check_loss()
        if len(powerups) != 0:
            for powerup in powerups:
                canvas.move(powerup, 0, 7)
        check_powerups()
        root.after(40, game_loop)





reset()
root.mainloop()