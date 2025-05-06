from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

ball.x_move = 4
ball.y_move = 4

PADDLE_SPEED = 30  # Augmenté de 20 à 30

def r_paddle_up():
    if r_paddle.ycor() < 250:
        r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() + PADDLE_SPEED)

def r_paddle_down():
    if r_paddle.ycor() > -240:
        r_paddle.goto(r_paddle.xcor(), r_paddle.ycor() - PADDLE_SPEED)

def l_paddle_up():
    if l_paddle.ycor() < 250:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() + PADDLE_SPEED)

def l_paddle_down():
    if l_paddle.ycor() > -240:
        l_paddle.goto(l_paddle.xcor(), l_paddle.ycor() - PADDLE_SPEED)

screen.listen()
screen.onkey(r_paddle_up, "Up")
screen.onkey(r_paddle_down, "Down")
screen.onkey(l_paddle_up, "w")
screen.onkey(l_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed * 0.3)  # Accélération de la balle
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
