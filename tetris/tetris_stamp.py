"""Painting Part"""

from turtle import Turtle


PAD_TOP = 150
PAD_X = 190

COLORS = ["green", "red", "blue", "yellow", "lightblue", "purple"]


class Stamp(Turtle):
    """docs"""

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(COLORS[0])
        self.speed(0)

    def draw_screen(self, width, height, grid):
        """Every loop it is called to draw the grid according column value"""
        top = height // 2 - (PAD_TOP)
        left = -(width // 2) + (PAD_X)

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                screen_x = left + (x * 20)
                screen_y = top - (y * 20)
                self.goto(screen_x, screen_y)
                if cell:
                    self.color(COLORS[cell])
                else:
                    self.color(COLORS[0])
                self.stamp()
