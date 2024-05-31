"""Block"""

from turtle import Turtle

matrix = [["X" for _ in range(3)] for _ in range(3)]
print(matrix)

BINS = (0, -500)


class Block(Turtle):
    """docs"""

    colors = ["red", "blue", "green", "yellow", "purple"]

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.length = 3
        self.shapesize(stretch_len=self.length, stretch_wid=2)

    def move_to_bin(self):
        """docs"""
        self.color("white")
        self.goto(BINS)
        del self

    def move_down(self, move_by=20):
        """docs"""
        x_cor, y_cor = self.position()
        new_y_cor = y_cor - move_by
        self.goto(x_cor, new_y_cor)
