"""Shape in tetris"""

import time
from grid_lines import Square

SHAPES = """
[x,y][x+z,y][x+2z,y][x+3z,y]

    [x+z ,y+z]
[x, y][x+z, y][x, y]

[x,   y][x+z,   y][x+2z,   y]
[x, y-z][x+z,y- z][x+2z, y-z]
[x,y-2z][x+z,y-2z][x+2z,y-2z]
"""

MATRIX = {"line": []}


class Shape:
    """docs"""

    def __init__(self):
        self.shapes = []
        self.colors = ["red", "blue", "green", "yellow"]
        self.create_line()
        self.create_cube()

    def create_line(self):
        """docs"""
        line = []
        for i in range(4):
            blocks = Square()
            print(blocks.starting_point)
            blocks.squares = [square.color(self.colors[i]) for square in blocks.squares]
            width, _ = blocks.get_distance()
            x_cor, y_cor = Square.starting_point
            Square.starting_point = (x_cor + 2 * width), y_cor
            line.append(blocks)
        self.shapes.append({"line": line})

    # [x,   y][x+z,   y][x+2z,   y]
    # [x, y-z][x+z,y- z][x+2z, y-z]
    # [x,y-2z][x+z,y-2z][x+2z,y-2z]

    def create_cube(self):
        """docs"""
        cube = []
        colors = self.colors * 3
        square = Square()
        width, height = square.get_distance()
        center = Square.starting_point
        coordinates = [
            (center[0] + width * x * 2, center[1] - height * y * 2)
            for y in range(3)
            for x in range(3)
        ]
        for i, coordinate in enumerate(coordinates):
            Square.starting_point = coordinate
            blocks = Square()
            blocks.squares = [block.color(colors[i]) for block in blocks.squares]
            cube.append(blocks)
