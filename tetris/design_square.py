"""Squre"""

from turtle import Turtle

SQUARE = """
(x,y)(x+distance + y)
(x, y-distance), (x+distance, y-distance)
"""


class Square:
    """Design of Unit as circle"""

    center = (0, 0)

    def __init__(self, width=1, height=1, outline=1):
        self.width = width
        self.height = height
        self.outline = outline
        self.squares = []
        self.create_square()

    def create_square(self):
        """doc"""
        for _ in range(4):
            square = Turtle(shape="square")
            # square.penup()
            square.shapesize(self.height, self.width, self.outline)
            width = self.width * 10
            height = self.height * 10
            square.color("red")
            if not self.squares:
                square.goto(Square.center)
            elif len(self.squares) == 1:
                square.goto(Square.center[0] + (2 * width), Square.center[1])
            elif len(self.squares) == 2:
                square.goto(Square.center[0], Square.center[1] - (2 * height))
            elif len(self.squares) == 3:
                square.goto(
                    Square.center[0] + (2 * width), Square.center[1] - (2 * height)
                )
            self.squares.append(square)
