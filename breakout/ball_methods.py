"""Ball Class Attributes and Methods"""

from turtle import Turtle


class Ball(Turtle):
    """docs"""

    left_or_right = [-1, 1]

    def __init__(self, default_position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(default_position)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """docs"""
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

    # def reset_position(self, position):
    #     """docs"""
    #     x_cor, y_cor = position
    #     self.goto(x_cor, y_cor + 30)
    #     self.ball_speed = 0.1
    #     self.bounce_x()
