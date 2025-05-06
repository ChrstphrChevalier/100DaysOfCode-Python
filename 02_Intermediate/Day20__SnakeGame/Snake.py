from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Initialiser le serpent avec 3 segments."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Déplacer chaque segment du serpent."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changer l'orientation du serpent vers le haut."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changer l'orientation du serpent vers le bas."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changer l'orientation du serpent vers la gauche."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changer l'orientation du serpent vers la droite."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        """Ajouter un segment au serpent."""
        last_segment = self.segments[-1]
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)
