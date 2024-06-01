"""
Designing shape as Matrix helps to manupulate the Shapes
"""

import random
from squares import Turtle
from matrixies import SHAPES

BINS = (-400, 0)


class Shape:
    """docs"""

    center = (0, 200)

    def __init__(self, width=1, height=1) -> None:
        self.width = width
        self.height = height
        self.shapes = {}
        self.colors = ["red", "blue", "green", "yellow"]
        self.distance = (width * 10 * 2, height * 10 * 2)

    def random_choose(self):
        """docs"""
        return list(SHAPES.keys())

    def create_the_shape(self, shape_name):
        """docs"""
        matrix = SHAPES[shape_name]
        self.set_the_shape(shape_name, matrix)

    def create_square(self):
        """docs"""
        square = Turtle(shape="square")
        square.penup()
        square.goto(Shape.center[0] - 60, Shape.center[1])
        square.shapesize(stretch_len=self.height, stretch_wid=self.width, outline=2)
        return square

    def set_the_shape(self, shape_name, matrix):
        """docs"""
        lst = []
        color = random.choice(self.colors)
        x_cor, y_cor = Shape.center
        x_len, y_len = self.distance
        for y, row in enumerate(matrix):
            for x, value in enumerate(row):
                square = self.create_square()
                square.color(color)
                if y == 0 and value:
                    square.goto(x_cor + x * x_len, y_cor)
                elif y >= 1 and value:
                    square.goto(x_cor + x * x_len, y_cor - y * y_len)
                lst.append(square)
        self.shapes[shape_name] = {"matrix": matrix, "turtles": lst}

    def clockwise(self, shape_name):
        """docs"""
        matrix = self.shapes.get(shape_name).get("matrix")
        turtles = self.shapes[shape_name]["turtles"]
        transpose = list(zip(*matrix))
        rotation = [list(reversed(row)) for row in transpose]
        self.set_the_shape(shape_name, rotation)
        self.remove_old_view(turtles)

    def move(self, shape_name):
        """docs"""
        move_by = 5
        turtles = self.shapes[shape_name]["turtles"]
        reversed_turtles = list(reversed(turtles))
        for square in reversed_turtles:
            square.goto(square.xcor(), square.ycor() - move_by)

    def remove_old_view(self, turtles: list):
        """docs"""
        for square in turtles:
            square.goto(BINS)
