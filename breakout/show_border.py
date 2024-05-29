"""test for breakut window boundry"""

from turtle import Turtle

WIDTH = 800
HEIGHT = 600
X_HALF = WIDTH // 2
Y_HALF = HEIGHT // 2
border = {"upper": 10, "bottom": 25, "sides": 10}


class Border(Turtle):
    """docs"""

    def __init__(self):
        super().__init__()
        self.color("white")

    def default_setheading(self):
        """docs"""
        self.setheading(0)

    def bottom_line(self, distance=800):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-X_HALF, -(Y_HALF - border["bottom"]))
        self.pendown()
        self.forward(distance)

    def upper_line(self, distance=800):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-X_HALF, (Y_HALF - border["upper"]))
        self.pendown()
        self.forward(distance)

    def left_line(self):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto(-(X_HALF - border["sides"]), -(Y_HALF - (border["bottom"])))
        self.left(90)
        self.pendown()
        self.forward(HEIGHT - (border["bottom"] + border["upper"]))

    def right_line(self):
        """docs"""
        self.penup()
        self.default_setheading()
        self.goto((X_HALF - border["sides"]), -(Y_HALF - (border["bottom"])))
        self.left(90)
        self.pendown()
        self.forward(HEIGHT - (border["bottom"] + border["upper"]))
