import turtle
from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.instances = []
        self.make_snake()
        self.head = self.instances[0]

    def make_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move_snake(self):
        for turtle in range(len(self.instances) - 1, 0, -1):
            x_cordi = self.instances[turtle - 1].xcor()
            y_cordi = self.instances[turtle - 1].ycor()
            self.instances[turtle].goto(x_cordi, y_cordi)
        self.head.forward(MOVE_DIST)

    def add_segment(self, position):
        t1 = Turtle()
        t1.penup()
        t1.color("white")
        t1.shape("square")
        t1.goto(position)
        self.instances.append(t1)

    def extend(self):
        self.add_segment(self.instances[-1].position())

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

    def reset(self):
        for instance in self.instances:
            instance.goto(1000, 1000)
        self.instances.clear()
        self.make_snake()
        self.head = self.instances[0]