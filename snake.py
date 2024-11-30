from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for turtle in range(0, 3):
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(POSITION[turtle])
            self.segments.append(t)

    def move(self):
        for turtle in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[turtle - 1].xcor()
            new_y = self.segments[turtle - 1].ycor()
            self.segments[turtle].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def update_snake(self):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(self.segments[-1].position())
        self.segments.append(t)
