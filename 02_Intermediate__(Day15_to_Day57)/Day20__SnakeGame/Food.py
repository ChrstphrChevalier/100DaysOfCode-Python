from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Placer la nourriture à une nouvelle position aléatoire."""
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
