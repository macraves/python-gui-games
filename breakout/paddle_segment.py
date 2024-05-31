"""List of Turtles Paddle"""

from turtle import Turtle
from random import choice

MOVE_BY = 20


class Paddles:
    """docs"""

    def __init__(self, positions):
        self.segments = []
        # self.colors = ["white"] * 5
        self.colors = ["red", "blue", "green", "yellow", "purple"]
        self.default_positions = positions
        self.initiliazer()

    def add_segments(self, position, color=None):
        """docs"""
        if color is None:
            color = choice(self.colors)
        if self.colors:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color(color)
            segment.shapesize(stretch_len=1)
            segment.goto(position)
            self.segments.append(segment)
        else:
            self.colors = ["red", "blue", "green", "yellow", "purple"]

    def initiliazer(self):
        """docs"""
        for i, postion in enumerate(self.default_positions):
            self.add_segments(postion, self.colors[i])

    def go_right(self, boundry):
        """docs"""
        head = self.segments[-1]
        head.setheading(0)
        if head.xcor() + 20 < boundry:
            for i in range(len(self.segments) - 1):
                new_x = self.segments[i + 1].xcor()
                new_y = self.segments[i + 1].ycor()
                self.segments[i].goto(new_x, new_y)
            head.forward(MOVE_BY)

    def go_left(self, boundry):
        """docs"""
        head = self.segments[0]
        head.setheading(180)
        if head.xcor() - 20 > -boundry:
            for i in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[i - 1].xcor()
                new_y = self.segments[i - 1].ycor()
                self.segments[i].goto(new_x, new_y)
            head.forward(MOVE_BY)

    def extend(self):
        """docs"""
        if self.colors and len(self.segments) < 10:
            color = self.colors.pop()
            self.add_segments(self.segments[-1].position(), color=color)

    def shrink(self):
        """docs"""
        if len(self.segments) > 5:
            segment = self.segments.pop()
            segment.goto(0, -500)
            segment.color("black")
            del segment
