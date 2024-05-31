"""Paddle"""

from turtle import Turtle

UNIT = 60
PAD_BORDER = 95


class Paddle(Turtle):
    """docs"""

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.goto(0, -290)

    def go_right(self, boundry):
        """Right movement"""
        if self.xcor() + PAD_BORDER < boundry:
            new_x = self.xcor() + UNIT
            self.goto(new_x, self.ycor())

    def go_left(self, boundry):
        """Left movement"""
        if self.xcor() - PAD_BORDER > -boundry:
            new_x = self.xcor() - UNIT
            self.goto(new_x, self.ycor())
