import turtle as t
import colors as c
import random

t.colormode(255)
Franklin = t.Turtle()
Franklin.speed("fastest")
Franklin.penup()
Franklin.hideturtle()
Franklin.setheading(225)
Franklin.forward(300)
Franklin.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    Franklin.dot(20, random.choice(c.colors))
    Franklin.forward(50)

    if dot_count % 10 == 0:
        Franklin.setheading(90)
        Franklin.forward(50)
        Franklin.setheading(180)
        Franklin.forward(500)
        Franklin.setheading(0)

screen = t.Screen()
screen.exitonclick()