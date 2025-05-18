import turtle
import random
import time

# --- Fenêtre ---
win = turtle.Screen()
win.title("Breakout")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# --- Paddle ---
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# --- Balle ---
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 2
ball.dy = 2
ball.speed_multiplier = 1.0

# --- Score & Vies ---
score = 0
lives = 3
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)

def update_display():
    score_display.clear()
    score_display.write(f"Score: {score}   Vies: {lives}", align="center", font=("Courier", 24, "normal"))

update_display()

# --- Blocs ---
blocks = []

def create_blocks():
    global blocks
    blocks.clear()
    colors = ["red", "orange", "green", "blue"]
    y = 250
    for color in colors:
        for i in range(8):
            block = turtle.Turtle()
            block.shape("square")
            block.color(color)
            block.shapesize(stretch_wid=1, stretch_len=4)
            block.penup()
            x = -350 + i * 100
            block.goto(x, y)
            blocks.append(block)
        y -= 30

create_blocks()

# --- Contrôles ---
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# --- Reset balle après perte de vie ---
def reset_ball():
    ball.goto(0, -200)
    ball.dx = 2 * (1 if random.choice([True, False]) else -1)
    ball.dy = 2
    ball.speed_multiplier = 1.0
    time.sleep(1)

# --- Reset jeu complet ---
def reset_game():
    global score, lives
    score = 0
    lives = 3
    update_display()
    create_blocks()
    paddle.goto(0, -250)
    reset_ball()

# --- Fin de partie ---
def game_over():
    message = turtle.Turtle()
    message.hideturtle()
    message.color("white")
    message.penup()
    message.goto(0, 0)
    message.write("Game Over\n[R] Rejouer  |  [Q] Quitter", align="center", font=("Courier", 20, "bold"))
    return message

# --- Boucle de jeu ---
running = True
while True:
    if not running:
        win.update()
        continue

    win.update()
    time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx * ball.speed_multiplier)
    ball.sety(ball.ycor() + ball.dy * ball.speed_multiplier)

    # Collisions mur
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        lives -= 1
        update_display()
        if lives == 0:
            msg = game_over()
            running = False

            def restart():
                global running
                msg.clear()
                reset_game()
                running = True

            def quit_game():
                win.bye()

            win.onkeypress(restart, "r")
            win.onkeypress(quit_game, "q")
        else:
            reset_ball()

    # Paddle
    if (ball.ycor() < -230 and paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Blocs
    for block in blocks:
        if (abs(ball.xcor() - block.xcor()) < 50 and abs(ball.ycor() - block.ycor()) < 20):
            ball.dy *= -1
            block.goto(1000, 1000)
            blocks.remove(block)
            score += 10
            ball.speed_multiplier += 0.05  # Augmentation progressive
            update_display()
            break

    # Victoire
    if not blocks:
        msg = turtle.Turtle()
        msg.hideturtle()
        msg.color("white")
        msg.penup()
        msg.goto(0, 0)
        msg.write("Bravo ! Tu as gagné 🎉\n[R] Rejouer  |  [Q] Quitter", align="center", font=("Courier", 20, "bold"))
        running = False

        def restart():
            global running
            msg.clear()
            reset_game()
            running = True

        def quit_game():
            win.bye()

        win.onkeypress(restart, "r")
        win.onkeypress(quit_game, "q")
