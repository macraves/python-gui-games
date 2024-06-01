"""Grid test"""

from turtle import Turtle
from square_large import Square


class Line(Turtle):
    """docs"""

    @staticmethod
    def get_center_sides_distance(square: Square):
        """docs"""
        x_value, y_value, _ = square.squares[0].shapesize()
        width_half, height_half = x_value * 10, y_value * 10
        return (width_half, height_half)

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")

    def draw_grid(self, go_to: tuple, distance):
        """docs"""
        self.goto(go_to)
        self.pendown()
        print(self.position())
        self.forward(distance)
        self.penup()

    def set_starting_point(self, index, var: dict, square: Square, distance):
        """docs"""
        x_cor, y_cor = square.squares[index].position()
        self.goto(x_cor, y_cor)
        half_width, half_height = self.get_center_sides_distance(square=square)
        new_x = x_cor + (half_width * var["x"])
        new_y = y_cor + (half_height * var["y"])
        self.draw_grid((new_x, new_y), distance=distance)

    def go_right(self, square: Square, distance=100):
        """docs"""
        top_right = 1
        self.setheading(0)
        var = {"x": 1, "y": 0}
        self.set_starting_point(top_right, var, square=square, distance=distance)

    def go_left(self, square: Square, distance=100):
        """docs"""
        top_left = 0
        self.setheading(180)
        var = {"x": -1, "y": 0}
        self.set_starting_point(top_left, var, square=square, distance=distance)

    def right_up(self, square: Square, distance=100):
        """docs"""
        bottom_right = 1
        self.setheading(90)
        var = {"x": 1, "y": 0}
        self.set_starting_point(bottom_right, var, square=square, distance=distance)

    def right_down(self, square: Square, distance=100):
        """docs"""
        bottom_right = 3
        self.setheading(270)
        var = {"x": 1, "y": 0}
        self.set_starting_point(bottom_right, var, square=square, distance=distance)

    def left_up(self, square: Square, distance=100):
        """docs"""
        bottom_right = 0
        self.setheading(90)
        var = {"x": -1, "y": 0}
        self.set_starting_point(bottom_right, var, square=square, distance=distance)

    def left_down(self, square: Square, distance=100):
        """docs"""
        bottom_right = 2
        self.setheading(270)
        var = {"x": -1, "y": 0}
        self.set_starting_point(bottom_right, var, square=square, distance=distance)
