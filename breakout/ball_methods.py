"""Ball Class Attributes and Methods"""

from random import choice
from turtle import Turtle


class Ball(Turtle):
    """docs"""

    width = 20
    height = 20
    view = "circle"
    left_or_right = [-1, 1]

    def __init__(self):
        super().__init__()
        self.shape(Ball.view)
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.default_position = (0, -260)
        self.goto(self.default_position)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """docs"""
        # direction = choice(Ball.left_or_right)
        nex_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(nex_x, new_y)

    def bounce_y(self):
        """Reverse y cor"""
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        """Reverse x cor"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """docs"""
        self.goto(self.default_position)
        self.ball_speed = 0.1
        self.bounce_x()
