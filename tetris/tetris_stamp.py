"""Painting Part"""

from turtle import Turtle


PAD_TOP = 150
PAD_X = 190


class Stamp(Turtle):
    """docs"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.default_color = "green"
        self.color(self.default_color)
        self.speed(0)

    def draw_grid(self, width, height, shape, grid, size=1):
        """docs"""
        top = height // 2 - (PAD_TOP // size)
        left = -(width // 2) + (PAD_X // size)

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                screen_x = left + (x * 20 * size)
                screen_y = top - (y * 20 * size)
                self.goto(screen_x, screen_y)
                self.stamp()
